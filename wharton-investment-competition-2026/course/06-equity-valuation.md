# Module 6 · Equity valuation

A company's value is the present value of the cash it will generate; its price is what the market charges today. Buy when your estimate of value sits comfortably above the price, and show judges which assumptions drive the gap.

## 6.1 The four approaches

| Approach | Methods | Best for | Weakness |
| --- | --- | --- | --- |
| Intrinsic | Discounted cash flow (DCF), dividend discount model (DDM), residual income | Predictable cash flows | Very sensitive to the discount rate and terminal growth |
| Relative | P/E, EV/EBITDA, EV/sales, P/B, P/FCF, PEG, dividend yield | Quick cross-checks against peers | Inherits any mispricing of the peer group |
| Asset-based | Net asset value, liquidation value, sum of the parts | REITs, holding companies, conglomerates, distressed firms | Misses the value of a strong ongoing franchise |
| Market-implied | Reverse DCF | Testing what the current price assumes | Needs judgment about what is plausible |

## 6.2 Discounted cash flow, step by step

1. Forecast revenue, operating margin, taxes and reinvestment for 5–10 years.
2. Compute free cash flow to the firm (FCFF) for each year.
3. Discount each year's FCFF at the weighted average cost of capital (WACC, section 6.3).
4. Add a terminal value for all years after the forecast. Keep terminal growth at or below long-run nominal GDP growth; 2–3% is typical, and a rate close to WACC makes the value explode.
5. Enterprise value (EV) = present value of forecast FCFF + present value of the terminal value.
6. Equity value = EV − net debt − preferred stock − minority interests. Divide by diluted shares for value per share.
7. Run sensitivities on WACC and terminal growth, then compare with the price.

```math
FCFF = EBIT(1 - t) + D\&A - \text{Capex} - \Delta NWC \qquad TV_n = \frac{FCFF_n (1 + g)}{WACC - g}
```

**Worked example.** A company will generate FCFF of \$100M, \$108M, \$116M, \$124M and \$132M over five years. WACC is 8%, terminal growth 2.5%, net debt \$300M and diluted shares 50M.

| Year | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| FCFF (\$M) | 100 | 108 | 116 | 124 | 132 |
| Discount factor at 8% | 0.9259 | 0.8573 | 0.7938 | 0.7350 | 0.6806 |
| Present value (\$M) | 92.6 | 92.6 | 92.1 | 91.1 | 89.8 |

- Present value of the five years of cash flow: \$458.3M.
- Terminal value: 132 × 1.025 ÷ (0.08 − 0.025) = \$2,460.0M, worth \$1,674.2M today.
- Enterprise value \$2,132.5M − net debt \$300M = equity value \$1,832.5M, or **\$36.65 per share**.
- The terminal value is 78.5% of enterprise value. That share is typical, and it is why long-run assumptions dominate any DCF.

**Sensitivity of value per share**

| WACC \\ terminal growth | 2.0% | 2.5% | 3.0% |
| --- | --- | --- | --- |
| 7% | \$41.82 | \$46.30 | \$51.89 |
| 8% | \$33.71 | \$36.65 | \$40.18 |
| 9% | \$27.92 | \$29.97 | \$32.37 |

One point of WACC moves the value by roughly 20–25%. Present a range, not a single number.

## 6.3 The cost of capital

```math
r_e = r_f + \beta \times ERP \qquad WACC = \frac{E}{V} r_e + \frac{D}{V} r_d (1 - t)
```

- **Risk-free rate:** the 10-year Treasury yield, matched to the long horizon of the cash flows.
- **Beta:** a regression of the stock's returns on the market's (5 years of monthly or 2 years of weekly data), or a data provider's figure. Adjusted beta = 0.67 × raw beta + 0.33 pulls estimates toward 1.
- **Equity risk premium (ERP):** the extra return investors demand for owning stocks. Damodaran publishes an implied US ERP every month.
- **Cost of debt:** the yield to maturity on the company's bonds, or the risk-free rate plus a spread for its credit rating, taken after tax (the US federal corporate rate is 21%).
- **Weights:** use market values, not book values.
- **Example:** a 4.2% risk-free rate, a beta of 1.1 and a 5% ERP give a 9.7% cost of equity. With 80% equity, 20% debt costing 5.5% and a 21% tax rate, WACC = 8.63%.

## 6.4 The dividend discount model

```math
P_0 = \frac{D_1}{r - g}
```

- **Example:** next year's dividend is \$2.00, the required return 8% and growth 4%: value = \$50.00. At 5% growth it is \$66.67; at 3% it is \$40.00. One point of growth moves the value by 20–33%, so the model is only as good as its growth input.
- **Where it fits:** mature dividend payers such as utilities, consumer staples, banks and REITs. Use a two-stage version when today's high growth will slow, or the H-model when it fades steadily.

## 6.5 Relative valuation with multiples

Pick 4–8 genuinely comparable peers (same industry, similar growth, margins, size and risk). Compute their multiples on the same basis, trailing or forward, and take the median. Apply it to your company's metric, adjust for differences in growth and quality, and cross-check with a DCF.

| Multiple | Best for | Caution |
| --- | --- | --- |
| P/E | Mature, profitable companies | Distorted by leverage, one-off items and buybacks; peak-cycle earnings make cyclicals look cheap |
| EV/EBITDA | Firms with different debt levels; capital-intensive industries | Ignores capex and taxes |
| EV/sales | Unprofitable or early-stage companies | Ignores profitability entirely |
| P/B | Banks and insurers | Meaningless for asset-light firms |
| P/FFO or P/AFFO | REITs | Definitions vary between REITs |
| FCF yield (FCF ÷ market cap) | Cash-generative businesses | Lumpy capex distorts single years |
| PEG (P/E ÷ growth rate) | Comparing growth companies | Growth estimates are uncertain |
| Dividend yield | Income stocks | A very high yield can signal a coming dividend cut |

**Justified multiples** link a multiple to fundamentals, so you can say whether a multiple is deserved:

```math
\text{Forward } P/E = \frac{\text{Payout ratio}}{r - g} \qquad P/B = \frac{ROE - g}{r - g}
```

With a 50% payout, an 8% required return and 4% growth, the justified forward P/E is 12.5×; a stock at 25× needs much faster growth or much lower risk to deserve it. With a 12% ROE the justified P/B is 2.0×, and a company whose ROE merely equals its cost of equity deserves to trade at book value.

## 6.6 Reverse DCF: what is the market assuming?

Start from the price and solve for the growth or margins it implies, then ask whether that is believable given the company's history, its industry and its competition. In a spreadsheet, use Goal Seek to set value per share equal to today's price by changing the growth rate.

The dividend model gives a quick version: implied growth = r − D1 ÷ P0. A \$60 stock paying a \$2 dividend with an 8% required return implies 4.7% dividend growth forever. That is above long-run nominal GDP growth, so the price looks demanding. Reverse DCFs turn an argument about a number into an argument about the business, which judges find persuasive.

## 6.7 Other methods

- **Residual income:** value = book value today + present value of future (ROE − cost of equity) × book value. Useful for banks and companies that pay no dividend.
- **Sum of the parts:** value each segment with its own method or multiple, then subtract net debt and unallocated corporate costs. Useful for conglomerates.
- **Net asset value:** the market value of assets minus liabilities. Useful for REITs and holding companies.

## 6.8 Margin of safety and presenting value

- **Margin of safety** = (intrinsic value − price) ÷ intrinsic value. As a rule of thumb, ask for 25–40% on uncertain businesses and 10–20% on stable ones.
- **Football field:** a chart of horizontal bars showing the value range from each method (DCF, comparables, DDM, 52-week trading range), with the current price as a vertical line. It is the standard valuation exhibit in a report.
- **Upside and downside:** state the upside to your base case and the downside to your bear case. For a conservative client, the downside matters more.

## 6.9 Common valuation mistakes

- Terminal growth above long-run nominal GDP, or close to WACC.
- Mismatching cash flows and discount rates: FCFF with the cost of equity, or nominal cash flows with real rates.
- Ignoring stock-based compensation and dilution.
- Double-counting growth with both high forecast growth and a high exit multiple.
- Valuing cyclical companies on peak earnings.
- False precision: \$36.65 is a point inside a range of roughly \$30 to \$46.
- Anchoring on today's price or on analysts' targets.

## Apply it to your case

- Value every stock with at least two methods (a DCF or DDM plus multiples) and include a sensitivity table.
- For a conservative client, favor businesses where even the bear case sits close to today's price. Limited downside is the point.

---

[← Module 5 · Analyzing company growth](05-analyzing-company-growth.md) · [Course contents](README.md) · [Module 7 · Fixed income and TIPS →](07-fixed-income-and-tips.md)
