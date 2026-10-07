# Appendix · Worked example: from client file to finished portfolio

This fictional case runs the whole course end to end, so your team can see what a finished analysis looks like. The client is invented and the return assumptions are illustrative; the method is what to copy. The result: a 33%-stock portfolio that expects 4.86% a year against a 4.42% requirement and keeps every stress-test loss inside the client's 10% limit.

## A.1 The client file

Helena Park (fictional), 55, is a hospital administrator with a stable salary and one adult daughter.

- **Investable assets:** \$500,000, of which \$300,000 is in a taxable brokerage account and \$200,000 in a traditional IRA. A \$40,000 emergency fund sits in savings, outside the portfolio.
- **Savings:** \$12,000 a year into the taxable account.
- **Goals:** (1) give her daughter \$50,000 toward a home down payment in 3 years; (2) retire at 65 with about \$850,000, enough to draw roughly \$34,000 a year at a 4% withdrawal rate alongside Social Security and a small pension; (3) leave a gift to her local library, a wish rather than a need.
- **Taxes:** 24% federal and 5% state brackets.
- **In her words:** "I watched my 401(k) drop by a third in 2008 and couldn't sleep for months. I never want to lose more than 10% in a year." "Groceries cost a fortune now. I don't want inflation eating my savings." "Please, nothing in tobacco or weapons."

## A.2 Diagnosis

```math
500{,}000\,(1+r)^{10} + 12{,}000\,\frac{(1+r)^{10}-1}{r} - 50{,}000\,(1+r)^{7} = 850{,}000 \;\Rightarrow\; r = 4.42\%
```

She needs 4.42% a year, about 1.9% after 2.5% inflation.

| Dimension | Assessment | Evidence |
| --- | --- | --- |
| Willingness | Low | An explicit 10% loss limit; her 2008 experience |
| Ability | Moderate to high | 10 years to retirement, stable income, an emergency fund, steady saving |
| Need | Moderate | A 4.42% required return |
| Overall | Conservative | Willingness is the binding constraint, and her ability and need do not demand more risk |

## A.3 IPS summary

| Element | Policy |
| --- | --- |
| Return | At least 4.5% a year on average over rolling 5-year periods after fees (about 2% real), enough to fund the \$850,000 goal |
| Risk | Below-average tolerance: no calendar-year loss above 10% (\$50,000) in severe-but-plausible stress tests; expected volatility of 5–7%; 95% one-year VaR below 8% |
| Time horizon | Three stages: 3 years to the gift, 10 years to retirement, then 25+ years of withdrawals |
| Liquidity | \$50,000 in T-bills in the taxable account for the gift; emergency fund kept outside the portfolio |
| Taxes | Bonds and TIPS in the IRA. T-bills, short Treasuries (free of state tax), tax-efficient stock funds and gold in the taxable account. No IRA withdrawals before 59½, when a 10% penalty generally applies |
| Legal and regulatory | None beyond fiduciary standards |
| Unique circumstances | Exclude tobacco and weapons makers; prefers income and simplicity |
| Allocation | Stocks 33% (range 28–38%), bonds and cash 62% (57–67%), gold 5% (3–7%) |
| Rebalancing | Check monthly; rebalance any sleeve more than 3 points from target, and the whole portfolio at least once a year, using new savings first |

## A.4 Capital market assumptions (illustrative)

These are teaching numbers. In your report, cite a published set ([Module 12](12-portfolio-theory-and-asset-allocation.md)).

| Sleeve | Expected return | Volatility |
| --- | --- | --- |
| T-bills | 3.3% | 0.5% |
| Short-term Treasuries (1–3 years) | 3.6% | 1.8% |
| Short-term TIPS (0–5 years) | 3.8% | 2.5% |
| Core investment-grade bonds | 4.6% | 5.5% |
| US dividend-growth stocks | 6.3% | 14.5% |
| US broad market | 6.5% | 16.5% |
| International developed stocks | 7.2% | 17.0% |
| Gold | 4.0% | 15.0% |

Correlations assumed: 0.80–0.95 among the stock sleeves, about 0.1 between stocks and bonds (−0.1 for short Treasuries), 0.6–0.8 among the bond sleeves, and 0.05–0.30 between gold and everything else.

## A.5 The portfolio

| Sleeve | Weight | Amount | Account | How to implement | Role |
| --- | --- | --- | --- | --- | --- |
| T-bills | 10% | \$50,000 | Taxable | SGOV or BIL | Funds the gift in year 3 |
| Short-term Treasuries | 13% | \$65,000 | \$60,000 taxable, \$5,000 IRA | VGSH or SHY | Stability and liquidity; interest free of state tax |
| Short-term TIPS | 14% | \$70,000 | IRA | VTIP or STIP | Inflation protection with little rate risk |
| Core investment-grade bonds | 25% | \$125,000 | IRA | BND or AGG | Income and recession ballast |
| US dividend-growth stocks | 13% | \$65,000 | Taxable | Six individual dividend growers that pass her screen, about 2% each | Quality stocks with rising income |
| US broad market, screened | 12% | \$60,000 | Taxable | ESGV, whose index excludes tobacco and weapons makers (verify the methodology) | Low-cost market growth within her values |
| International developed stocks, screened | 8% | \$40,000 | Taxable | A developed-markets fund screened for her exclusions | Diversification |
| Gold | 5% | \$25,000 | Taxable | GLDM or IAU | Crisis and inflation hedge |

The dividend sleeve uses individual stocks because popular dividend-growth ETFs hold some companies she excludes, such as defense contractors. That turns a constraint into a chance to show stock research.

## A.6 Risk check

The portfolio's expected return is 4.86% with expected volatility of 5.65%, a Sharpe ratio of 0.28 against T-bills. Its 95% one-year VaR is 4.4%, about \$22,200.

**Stress tests.** Scenario returns are rounded approximations of broad-index calendar-year results for 2008 and 2022, plus a hypothetical stagflation year; verify any figure before citing it.

| Sleeve | Weight | 2008-style crash | 2022-style inflation shock | Hypothetical stagflation |
| --- | --- | --- | --- | --- |
| T-bills | 10% | +1.4% | +2.0% | +4.0% |
| Short-term Treasuries | 13% | +6.6% | −3.8% | +1.0% |
| Short-term TIPS | 14% | −2.5% | −2.7% | +3.0% |
| Core bonds | 25% | +5.2% | −13.0% | −6.0% |
| US dividend growers | 13% | −27% | −10% | −15% |
| US broad market | 12% | −37% | −19.5% | −20% |
| International developed | 8% | −43% | −14.5% | −22% |
| Gold | 5% | +4.0% | +0.5% | +15% |
| **Portfolio** | 100% | **−9.2% (−\$46,200)** | **−8.7% (−\$43,500)** | **−5.9% (−\$29,600)** |
| A 60/40 mix of the same sleeves |  | −19.0% | −12.1% | −12.2% |

Every scenario stays inside her 10% limit, though the 2008-style test comes close. That is why stocks stop at 33%.

**Where the risk really sits.** Stocks are 33% of the money but about 82% of the expected risk; bonds and cash are 62% of the money and about 14% of the risk; gold contributes about 4%.

## A.7 Will it reach the goal?

A Monte Carlo simulation ran 100,000 ten-year paths from the assumptions above, adding \$12,000 a year and withdrawing \$50,000 in year 3. The portfolio reached \$850,000 in **56%** of paths. The median outcome was \$871,000, with \$672,000 at the 5th percentile and \$1,135,000 at the 95th.

| Change | Probability of reaching the goal | Worst stress-test loss |
| --- | --- | --- |
| Proposed portfolio | 56% | −9.2% |
| Raise stocks to 40% | 58% | −11.9%, breaking her limit |
| Save \$18,000 a year instead of \$12,000 | 76% | −9.2% |
| Retire at 66 instead of 65 | 69% | −9.2% |
| Aim for \$800,000 instead of \$850,000 | 71% | −9.2% |
| All cash and short-term bonds | 1% | −1.2% |

For a conservative client, more risk is the weakest lever: raising stocks to 40% adds 2 points of probability and breaks her loss limit, while saving \$500 more a month adds 20 points. The adviser's job is to lay out these trade-offs and let her choose.

## A.8 Monitoring plan

- **Monthly:** check drift against the ranges and update the risk dashboard.
- **Quarterly:** send the client report and review each stock against its sell criteria.
- **Annually:** rebalance fully; update the assumptions, the required return and the Monte Carlo; review the IPS.
- **Triggers for an early review:** the gift date moves, her job changes, inflation or real yields move sharply (re-check the TIPS share), or losses for the year approach 8%. Call her before she calls you.
- **The road ahead:** the T-bills fund the gift in year 3. In years 7–10, build a two-to-three-year spending bucket and consider a TIPS ladder for her first years of withdrawals.

## A.9 Adapting this to the Laura Gao case

1. Replace every input with facts from the Laura Gao file: assets, savings, goals, dates, taxes and her own words.
2. Recompute her required return and her loss limit. Let them, not this example, set the weights.
3. Cite a published set of capital market assumptions, then rerun the stress tests and the Monte Carlo in a spreadsheet or Portfolio Visualizer.
4. Keep the structure: diagnosis → IPS → allocation → holdings → risk check → probability of success → monitoring.

---

[← Module 16 · Competition playbook](16-competition-playbook.md) · [Course contents](README.md) · [Sources →](sources.md)
