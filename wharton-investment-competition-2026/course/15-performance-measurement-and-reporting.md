# Module 15 · Performance measurement, monitoring and client reporting

Measure performance the right way: time-weighted returns to judge the manager, money-weighted returns to show the client's own experience. Compare results with the right benchmark, explain where they came from, and report them in plain English.

## 15.1 Time-weighted vs money-weighted returns

- **Time-weighted return (TWR):** links the returns of each sub-period between cash flows, so the timing of the client's deposits and withdrawals does not affect it. It measures the manager's skill and is required by the Global Investment Performance Standards (GIPS) for most reporting.
- **Money-weighted return (MWR):** the internal rate of return of all cash flows. It reflects the client's actual experience, including the timing of their deposits.

```math
TWR = \left[\prod_{i=1}^{n}(1 + r_i)\right]^{1/\text{years}} - 1
```

**Example.** A client starts with \$100,000. Year 1 returns +10%, taking the account to \$110,000. She then adds \$50,000, making \$160,000, and year 2 returns −5%, ending at \$152,000.

- TWR: (1.10 × 0.95)^½ − 1 = **2.23% a year** (4.5% cumulative).
- MWR: solve 100,000(1 + r)² + 50,000(1 + r) = 152,000, giving **0.80% a year**.
- The manager earned 2.23% a year, but the client earned less because she added money just before the losing year. Both numbers are correct; they answer different questions.

## 15.2 Reporting conventions

- **Annualize** returns for periods longer than a year; never annualize a period shorter than a year.
- **Gross vs net:** report both before and after fees.
- **Before vs after tax, nominal vs real:** the client lives on after-tax, after-inflation returns.
- **Geometric, not arithmetic,** for multi-year averages ([Module 1](01-investment-foundations.md)).
- **Same period, same basis:** compare portfolio and benchmark over identical dates.

## 15.3 Benchmarks

- **Policy benchmark:** the IPS target weights applied to an index for each asset class. It answers whether the implementation beat simply holding the plan.
- **Asset-class benchmarks:** each sleeve against its own index, such as US stocks against the S&P 500 or bonds against the Bloomberg US Aggregate.
- **Absolute or goal benchmark:** CPI + 2%, or the required return. It answers whether the client is on track.
- **Peer groups:** fund-category averages are useful context but suffer from survivorship bias.
- **Excess (active) return** = portfolio return − benchmark return.

## 15.4 Risk-adjusted performance

| Measure | Formula | Use it to |
| --- | --- | --- |
| Sharpe ratio | (Return − risk-free rate) ÷ volatility | Compare total-risk efficiency across portfolios |
| Sortino ratio | (Return − target) ÷ downside deviation | Focus on bad volatility, as a loss-averse client does |
| Treynor ratio | (Return − risk-free rate) ÷ beta | Judge a sleeve that sits inside a diversified portfolio |
| Jensen's alpha | Return − CAPM-required return | Measure value added after market risk |
| Information ratio | Active return ÷ tracking error | Judge skill relative to a benchmark |
| M² (Modigliani) | The return at the benchmark's volatility | Express the Sharpe ratio in percent |
| Calmar ratio | Annual return ÷ maximum drawdown | Judge return per unit of worst loss |
| Upside and downside capture | Portfolio return ÷ benchmark return, in up and down markets | Show a conservative client how much of the falls she avoided |

Two quick readings: an active return of 0.6% with 1.5% tracking error gives an information ratio of 0.4, which is respectable. Capturing 70% of the benchmark's gains but only 50% of its losses is exactly the profile a risk-averse client wants.

## 15.5 Performance attribution: where did the excess return come from?

The Brinson model splits excess return into three effects:

- **Allocation:** the result of over- or underweighting asset classes: (portfolio weight − benchmark weight) × benchmark return of that class.
- **Selection:** the result of picking securities within each class: benchmark weight × (portfolio return − benchmark return) of that class.
- **Interaction:** the combined effect: (weight difference) × (return difference).

**Example.** The portfolio holds 40% stocks returning 8% and 60% bonds returning 3%, for 5.0%. The benchmark holds 30% stocks returning 10% and 70% bonds returning 2%, for 4.4%. Excess return is 0.6 points.

| Effect | Stocks | Bonds | Total |
| --- | --- | --- | --- |
| Allocation | +1.0 | −0.2 | +0.8 |
| Selection | −0.6 | +0.7 | +0.1 |
| Interaction | −0.2 | −0.1 | −0.3 |
| Total | +0.2 | +0.4 | +0.6 |

Overweighting stocks in a year when they beat bonds added 0.8 points. Bond picking added 0.7, but stock picking cost 0.6. The interaction cost 0.3, because the portfolio overweighted the sleeve where its picks were weak. The Brinson–Fachler variant measures allocation against the total benchmark return; the total is the same, but the split between classes differs.

## 15.6 Monitoring

- **The client:** goals, income, health, family, taxes. Any change can change the IPS.
- **The markets:** the macro view and capital market assumptions, reviewed at least yearly.
- **The portfolio:** drift against IPS ranges, risk metrics against limits ([Module 14](14-risk-assessment-and-management.md) dashboard), and costs.
- **The holdings:** each thesis against its sell criteria, earnings results and news.
- **Frequency:** a monthly check of drift and risk, quarterly reporting, and an annual IPS review.

## 15.7 Client reporting

A good quarterly report contains:

1. Progress toward each goal, in dollars and as a probability of success.
2. Performance against the policy benchmark and the absolute target, net of fees.
3. The allocation against targets and ranges.
4. Risk metrics against the IPS limits.
5. Income received and expected.
6. Trades made and why.
7. A plain-English market commentary.
8. Next steps and decisions needed from the client.

Write for the client, not for other analysts. Explain bad quarters before the client asks, and connect every number to her goals.

## 15.8 In the competition

- Report the portfolio's return over the competition window against your policy benchmark over the same dates, and do not annualize a 10-week return.
- Explain the gaps with a simple attribution: allocation decisions vs security selection.
- Judges care more about whether your process was sound and true to the IPS than about the return itself. Own your mistakes and say what you learned.

## Apply it to your case

- Define Laura's policy benchmark now, so you can measure against it later.
- Track the portfolio weekly in a spreadsheet: value, return, benchmark return, drift and risk metrics.
- Draft the performance section of the final report as a client letter: progress first, numbers second, jargon never.

---

[← Module 14 · Risk assessment and management](14-risk-assessment-and-management.md) · [Course contents](README.md) · [Module 16 · Competition playbook →](16-competition-playbook.md)
