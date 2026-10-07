# Module 12 · Portfolio theory and asset allocation

The asset allocation drives most of a diversified portfolio's risk and its swings over time. Set the mix to the client's IPS first; choosing individual securities is a second-order decision.

## 12.1 Why allocation comes first

- **Brinson, Hood and Beebower (1986)** found that policy allocation explained about 94% of the variation in large US pension plans' quarterly returns over time.
- **Ibbotson and Kaplan (2000)** sharpened the claim: allocation explains about 90% of a fund's ups and downs over time, about 40% of the differences between funds, and roughly 100% of the level of return.
- **The lesson:** allocation sets the risk; selection fine-tunes it. Quote the research accurately and judges will notice.

## 12.2 Modern portfolio theory

Harry Markowitz (1952) showed that a portfolio's expected return is the weighted average of its parts, but its risk is not: whenever correlations are below 1, combining assets reduces risk.

```math
E(R_p) = \sum_i w_i\,E(R_i) \qquad \sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2\,w_1 w_2\,\rho_{12}\,\sigma_1\sigma_2
```

**Example.** Put 60% in stocks (expected return 7%, volatility 16%) and 40% in bonds (4%, 6%). Expected return is 5.8% whatever the correlation, but the risk changes:

| Stock-bond correlation | Portfolio volatility |
| --- | --- |
| +1.0 (no diversification) | 12.00% |
| +0.2 | 10.35% |
| 0.0 | 9.90% |
| −0.2 | 9.42% |

Lower correlation gives the same return with less risk. Diversification is the closest thing to a free lunch in finance.

- **Efficient frontier:** the set of portfolios with the highest expected return for each level of risk. Anything below it is inefficient; the minimum-variance portfolio sits at its left tip.
- **Capital allocation line:** mixing a risky portfolio with a risk-free asset. Its slope is the Sharpe ratio, and the tangency portfolio is the risky mix with the highest Sharpe ratio.
- **Risk aversion:** utility U = E(r) − ½ × A × σ², where A measures risk aversion. The best share in the risky portfolio is y\* = (E(r) − rf) ÷ (A × σ²). With an expected return of 7%, a risk-free rate of 4% and volatility of 16%, a client with A = 4 should hold about 29% in the risky portfolio, and one with A = 2 about 59%. A more risk-averse client sits closer to the risk-free asset.

## 12.3 CAPM and the security market line

```math
E(R_i) = r_f + \beta_i \left[E(R_m) - r_f\right]
```

- **Beta** measures sensitivity to market moves: covariance with the market ÷ the market's variance. A beta of 1 moves with the market, below 1 is defensive and above 1 is aggressive.
- **Example:** with a 4% risk-free rate, a beta of 0.8 and a 9% expected market return, the required return is 8%.
- **Alpha** is the actual return minus the CAPM-required return. Positive alpha means the investment beat what its risk deserved.
- **The key insight:** only systematic risk earns a premium, because diversifiable risk can be removed for free.
- **Limits:** beta is unstable and one factor misses much of what drives returns, which led to multi-factor models.

## 12.4 Factor models

- **Fama–French three-factor model:** market, size (small minus big, SMB) and value (high minus low book-to-market, HML). Carhart added momentum. The five-factor model adds profitability (robust minus weak, RMW) and investment (conservative minus aggressive, CMA).
- **Arbitrage pricing theory (Ross, 1976):** returns driven by several macro factors such as growth, inflation, interest rates and credit.
- **How to use them:** regress a fund's returns on factor returns to see what it really owns. A "dividend" fund may turn out to be a value and low-volatility tilt. Kenneth French's online data library supplies free factor returns, and Portfolio Visualizer runs the regressions.

## 12.5 Capital market assumptions

Allocation needs forward-looking expected returns, volatilities and correlations, known as capital market assumptions (CMAs).

- **Cash:** today's T-bill yield, adjusted for the expected path of Fed policy.
- **High-quality bonds:** the starting yield is the best single predictor of the next 5–10 years' return. For credit, subtract expected default losses.
- **Stocks (Grinold–Kroner):** expected return ≈ dividend yield + net buyback yield + real earnings growth + inflation + yearly change in valuation. For example, 1.5% + 0.5% + 2.0% + 2.5% − 0.5% = 6.0%.
- **Volatility and correlations:** start from long history, then adjust for the regime. Stock-bond correlation turns positive when inflation is the main risk ([Module 10](10-know-your-client.md)).
- **Cite a published set** rather than inventing numbers: Vanguard, BlackRock, J.P. Morgan's Long-Term Capital Market Assumptions, Research Affiliates and GMO all publish theirs.

## 12.6 Strategic, tactical and dynamic allocation

- **Strategic asset allocation (SAA):** the long-term policy mix in the IPS, rebalanced back to target.
- **Tactical asset allocation (TAA):** temporary tilts inside the IPS ranges based on valuations or the cycle, for example adding 3 points to short TIPS when inflation risk rises. Each tilt needs a reason and an exit.
- **Dynamic allocation or glide path:** the mix shifts as the client ages or a goal approaches, as in target-date funds.
- **Core-satellite:** a low-cost index core with satellites of individual stocks, active funds or factor tilts.

## 12.7 Allocation methods

| Method | How it works | Strengths | Weaknesses | Fit for a conservative client |
| --- | --- | --- | --- | --- |
| Mean-variance optimization | Maximizes expected return for each level of risk using CMAs | Rigorous, the industry standard | Very sensitive to inputs; extreme weights | Use with constraints and sensible ranges |
| Black–Litterman | Starts from market-cap weights, then blends in your views by confidence | Stable, intuitive weights | More complex | Good for justified tilts |
| Risk parity | Each asset contributes equal risk | Balanced risk exposure | Needs leverage to reach return targets; hurt in 2022 | The idea helps; the leverage does not |
| Equal weight (1/N) | The same weight in every asset | Simple and robust | Ignores differences in risk | Rarely |
| Goals-based buckets | Allocates money goal by goal, by horizon | Intuitive for clients | Can be less efficient overall | Excellent |
| Liability-driven investing | Matches assets to future spending (duration matching, TIPS ladders) | Funds needs with near-certainty | Lower expected return | Excellent for known spending |
| Rules of thumb | For example, 110 minus age in stocks | Quick | Ignores the actual client | A starting point only |
| Minimum variance or risk budgeting | Minimizes volatility, or sets a risk budget per asset | Low risk | Concentrates in low-volatility assets | A useful cross-check |

## 12.8 Model allocations by risk profile

Illustrative starting points, not recommendations. Tailor every weight to the IPS.

| Asset class | Conservative | Moderately conservative | Moderate | Growth |
| --- | --- | --- | --- | --- |
| Cash and T-bills | 10% | 5% | 5% | 2% |
| Short-term Treasuries and TIPS | 25% | 20% | 10% | 5% |
| Core bonds | 30% | 30% | 25% | 15% |
| US stocks | 20% | 27% | 38% | 50% |
| International stocks | 10% | 13% | 17% | 23% |
| Real assets (REITs, gold) | 5% | 5% | 5% | 5% |
| Total in stocks | 30% | 40% | 55% | 73% |

## 12.9 Diversification beyond asset classes

- **Geography:** the US is roughly 60% or more of world stock market value (approximate), yet investors everywhere overweight their home market.
- **Within asset classes:** sectors, factors, issuers, currencies and bond maturities.
- **Over time:** Vanguard research found that investing a lump sum beat dollar-cost averaging about two-thirds of the time, because markets rise more often than they fall. Averaging in can still help a nervous client commit.
- **Correlations rise in crises,** so match each diversifier to the kind of shock it protects against:

| Shock | What has tended to protect |
| --- | --- |
| Growth shock (recession) | High-quality government bonds, cash |
| Inflation shock | T-bills, short-duration bonds, short-term TIPS, commodities, trend-following |
| Financial or liquidity crisis | Cash, Treasuries, the US dollar |

## Apply it to your case

- Choose and cite a CMA source, and put your expected returns, volatilities and correlations in a table.
- Build two or three candidate allocations within Laura's IPS ranges. Compare expected return, volatility, stress-test loss and the probability of meeting her goal ([Module 14](14-risk-assessment-and-management.md)).
- Pick one and explain why it beats the alternatives for her, not in general.

---

[← Module 11 · Building the Investment Policy Statement](11-investment-policy-statement.md) · [Course contents](README.md) · [Module 13 · Portfolio construction and implementation →](13-portfolio-construction-and-implementation.md)
