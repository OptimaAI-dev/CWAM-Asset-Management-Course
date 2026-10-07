#!/usr/bin/env python3
"""Long-run US return statistics behind the course's history tables and chart.

Data: Aswath Damodaran (NYU Stern), annual returns 1928-2023, in data/.
Run:  python history.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).parent / "data" / "damodaran_annual_returns_1928_2023.csv"
df = pd.read_csv(DATA).set_index("Year") / 100  # percent -> decimal


def summary(r):
    """Compound return, volatility, worst year and number of losing years."""
    r = r.dropna()
    cagr = (1 + r).prod() ** (1 / len(r)) - 1
    return {
        "compound return": f"{cagr:.2%}",
        "arithmetic mean": f"{r.mean():.2%}",
        "volatility": f"{r.std(ddof=1):.2%}",
        "worst year": f"{r.min():.2%} ({r.idxmin()})",
        "losing years": f"{(r < 0).sum()} of {len(r)}",
    }


print("=== US asset classes, 1928-2023 ===")
for col, label in [("SP500", "S&P 500, dividends reinvested"), ("BaaCorp", "Baa corporate bonds"),
                   ("TBond10y", "10-year Treasury bonds"), ("TBill3m", "3-month Treasury bills")]:
    print(label, summary(df[col]))
print("Gold, 1971-2023", summary(df.loc[1971:, "Gold"]))

print("\n=== Stocks (S&P 500) mixed with 10-year Treasuries, rebalanced yearly ===")
rows = []
for stocks in range(0, 101, 10):
    w = stocks / 100
    mix = w * df["SP500"] + (1 - w) * df["TBond10y"]
    s = summary(mix)
    rows.append({"stocks": f"{stocks}%", **s})
print(pd.DataFrame(rows).to_string(index=False))

print("\n=== Stock-bond correlation by period ===")
for lo, hi in [(1928, 2023), (1928, 1999), (2000, 2021), (2000, 2023)]:
    sub = df.loc[lo:hi]
    print(f"{lo}-{hi}: {np.corrcoef(sub['SP500'], sub['TBond10y'])[0, 1]:+.2f}")
both = df[(df["SP500"] < 0) & (df["TBond10y"] < 0)].index.tolist()
print("Years when stocks and 10-year Treasuries both fell:", both)

gold = df.loc[1971:]
print(f"Gold vs stocks correlation, 1971-2023: {np.corrcoef(gold['SP500'], gold['Gold'])[0, 1]:+.2f}")
