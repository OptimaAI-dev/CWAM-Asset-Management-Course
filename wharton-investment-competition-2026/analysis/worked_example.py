#!/usr/bin/env python3
"""Reproduce the course's worked example (Appendix) and adapt it to your own client.

1. Edit the INPUTS section below (client numbers, weights, assumptions).
2. Run:  python worked_example.py

It prints the required return, the portfolio's expected return and risk, stress
tests in percent and dollars, where the risk comes from, a Monte Carlo
probability of reaching the goal, and a few what-if comparisons.

The return assumptions are illustrative teaching numbers. Replace them with a
published set of capital market assumptions before using results in a report.
"""
import numpy as np
from scipy.optimize import brentq

# ============================== INPUTS ==============================

START_VALUE = 500_000        # investable assets today ($)
ANNUAL_SAVINGS = 12_000      # added at the end of each year ($)
WITHDRAWALS = {3: 50_000}    # {year: amount} taken out at the end of that year ($)
GOAL = 850_000               # portfolio value the client needs ($)
YEARS = 10                   # years until the goal
INFLATION = 0.025            # used only to show the real required return
LOSS_LIMIT = 0.10            # largest acceptable calendar-year loss (IPS risk objective)
RISK_FREE = 0.033            # T-bill yield, for the Sharpe ratio

# name, weight, expected annual return, annual volatility
SLEEVES = [
    ("T-bills",                 0.10, 0.033, 0.005),
    ("Short-term Treasuries",   0.13, 0.036, 0.018),
    ("Short-term TIPS",         0.14, 0.038, 0.025),
    ("Core bonds",              0.25, 0.046, 0.055),
    ("US dividend growers",     0.13, 0.063, 0.145),
    ("US broad market",         0.12, 0.065, 0.165),
    ("International developed", 0.08, 0.072, 0.170),
    ("Gold",                    0.05, 0.040, 0.150),
]

# Correlation matrix, rows and columns in the same order as SLEEVES.
CORRELATIONS = np.array([
    [1.00,  0.30, 0.20, 0.10, 0.00,  0.00,  0.00, 0.00],
    [0.30,  1.00, 0.60, 0.80, -0.10, -0.10, -0.10, 0.20],
    [0.20,  0.60, 1.00, 0.60, 0.10,  0.10,  0.10, 0.30],
    [0.10,  0.80, 0.60, 1.00, 0.10,  0.10,  0.10, 0.30],
    [0.00, -0.10, 0.10, 0.10, 1.00,  0.95,  0.80, 0.05],
    [0.00, -0.10, 0.10, 0.10, 0.95,  1.00,  0.85, 0.05],
    [0.00, -0.10, 0.10, 0.10, 0.80,  0.85,  1.00, 0.15],
    [0.00,  0.20, 0.30, 0.30, 0.05,  0.05,  0.15, 1.00],
])

# Calendar-year returns in percent, same order as SLEEVES.
# The 2008 and 2022 rows are rounded approximations of broad-index results;
# verify any figure before citing it.
SCENARIOS = {
    "2008-style crash":           [1.4,  6.6, -2.5,   5.2, -27, -37.0, -43.0,  4.0],
    "2022-style inflation shock": [2.0, -3.8, -2.7, -13.0, -10, -19.5, -14.5,  0.5],
    "Hypothetical stagflation":   [4.0,  1.0,  3.0,  -6.0, -15, -20.0, -22.0, 15.0],
}

SIMULATIONS = 100_000
SEED = 42

# What-if comparisons: each entry overrides some of the inputs above.
WHAT_IFS = [
    ("Proposed portfolio", {}),
    ("Raise stocks to 40%", {"weights": [0.10, 0.10, 0.12, 0.23, 0.16, 0.14, 0.10, 0.05]}),
    ("Save $18,000 a year", {"savings": 18_000}),
    ("Retire one year later", {"years": YEARS + 1}),
    ("Aim for $800,000", {"goal": 800_000}),
    ("All cash and short-term bonds", {"weights": [0.40, 0.30, 0.30, 0, 0, 0, 0, 0]}),
]

# ============================ CALCULATIONS ============================

NAMES = [s[0] for s in SLEEVES]
WEIGHTS = np.array([s[1] for s in SLEEVES])
EXP_RET = np.array([s[2] for s in SLEEVES])
VOL = np.array([s[3] for s in SLEEVES])
COV = np.outer(VOL, VOL) * CORRELATIONS
SCEN = {k: np.array(v) / 100 for k, v in SCENARIOS.items()}


def future_value(r, start=START_VALUE, savings=ANNUAL_SAVINGS, years=YEARS, withdrawals=WITHDRAWALS):
    """Value after `years` at a constant return r, with year-end savings and withdrawals."""
    value = start
    for year in range(1, years + 1):
        value = value * (1 + r) + savings - withdrawals.get(year, 0)
    return value


def required_return(goal=GOAL, **kw):
    if future_value(0.0, **kw) >= goal:
        return 0.0
    return brentq(lambda r: future_value(r, **kw) - goal, 1e-9, 1.0)


def portfolio_stats(weights):
    w = np.asarray(weights, dtype=float)
    er = w @ EXP_RET
    sd = np.sqrt(w @ COV @ w)
    return er, sd


def risk_contributions(weights):
    w = np.asarray(weights, dtype=float)
    sd = np.sqrt(w @ COV @ w)
    return w * (COV @ w) / sd / sd  # shares of total volatility, summing to 1


def monte_carlo(weights, goal=GOAL, savings=ANNUAL_SAVINGS, years=YEARS, n=SIMULATIONS, seed=SEED):
    """Simulate yearly lognormal returns with the portfolio's mean and volatility."""
    er, sd = portfolio_stats(weights)
    sigma = np.sqrt(np.log(1 + (sd / (1 + er)) ** 2))
    mu = np.log(1 + er) - 0.5 * sigma ** 2
    rng = np.random.default_rng(seed)
    growth = np.exp(rng.normal(mu, sigma, (n, years)))
    value = np.full(n, float(START_VALUE))
    for t in range(years):
        value = value * growth[:, t] + savings - WITHDRAWALS.get(t + 1, 0)
    return (value >= goal).mean(), np.percentile(value, [5, 50, 95])


def money(x):
    return f"${x:,.0f}"


def main():
    assert abs(WEIGHTS.sum() - 1) < 1e-9, "Weights must sum to 100%"
    req = required_return()
    print("=== Client goal ===")
    print(f"Required return: {req:.2%} a year ({(1 + req) / (1 + INFLATION) - 1:.2%} after {INFLATION:.1%} inflation)")

    er, sd = portfolio_stats(WEIGHTS)
    var95 = 1.645 * sd - er
    print("\n=== Portfolio ===")
    print(f"Expected return: {er:.2%}   Expected volatility: {sd:.2%}   Sharpe ratio: {(er - RISK_FREE) / sd:.2f}")
    print(f"95% one-year value at risk: {var95:.2%} ({money(var95 * START_VALUE)})")
    print(f"Expected return {'covers' if er >= req else 'falls short of'} the required return.")

    print("\n=== Stress tests ===")
    for name, shocks in SCEN.items():
        r = WEIGHTS @ shocks
        flag = "within" if r >= -LOSS_LIMIT else "BREAKS"
        print(f"{name:<28} {r:+7.2%}  {money(r * START_VALUE):>10}   {flag} the {LOSS_LIMIT:.0%} loss limit")

    print("\n=== Where the risk comes from ===")
    rc = risk_contributions(WEIGHTS)
    for name, w, c in zip(NAMES, WEIGHTS, rc):
        print(f"{name:<26} weight {w:5.1%}   share of risk {c:5.1%}")

    prob, (p5, p50, p95) = monte_carlo(WEIGHTS)
    print(f"\n=== Monte Carlo ({SIMULATIONS:,} paths) ===")
    print(f"Chance of reaching {money(GOAL)} in {YEARS} years: {prob:.0%}")
    print(f"5th percentile {money(p5)}   median {money(p50)}   95th percentile {money(p95)}")

    print("\n=== What-ifs ===")
    print(f"{'Change':<32}{'Chance of goal':>15}{'Worst stress loss':>20}")
    for label, o in WHAT_IFS:
        w = np.array(o.get("weights", WEIGHTS), dtype=float)
        prob, _ = monte_carlo(w, goal=o.get("goal", GOAL), savings=o.get("savings", ANNUAL_SAVINGS),
                              years=o.get("years", YEARS))
        worst = min(w @ s for s in SCEN.values())
        print(f"{label:<32}{prob:>15.0%}{worst:>20.2%}")


if __name__ == "__main__":
    main()
