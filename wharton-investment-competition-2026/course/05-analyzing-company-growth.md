# Module 5 · Analyzing company growth

Growth creates value only when a company earns more on new capital than that capital costs. So measure growth carefully, test its quality and durability, then ask how much of it the price already assumes.

## 5.1 Measuring growth

```math
CAGR = \left(\frac{\text{Ending value}}{\text{Beginning value}}\right)^{1/n} - 1
```

- **Year-over-year (YoY):** this period ÷ the same period a year earlier − 1. Comparing a quarter with the same quarter last year removes seasonality.
- **CAGR:** EPS rising from \$2.00 to \$3.20 over 4 years is 12.5% a year.
- **Organic vs acquired:** strip out acquisitions and divestitures to see the underlying business.
- **Constant currency:** removes exchange-rate effects for multinationals.
- **Per share vs total:** net income can grow while EPS does not if the company issues shares. Owners care about per-share growth.
- **Every line:** measure growth in revenue, gross profit, EBIT, EPS, free cash flow, dividends and book value. When the lines diverge, find out why.

## 5.2 Worked example: Harbor Foods (fictional)

Harbor Foods has 150 million shares throughout; dollar figures are in millions except EPS.

| Measure | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | 4-year CAGR |
| --- | --- | --- | --- | --- | --- | --- |
| Revenue (\$M) | 4,000 | 4,240 | 4,452 | 4,719 | 5,000 | 5.7% |
| Revenue growth |  | 6.0% | 5.0% | 6.0% | 6.0% |  |
| Operating margin | 12.0% | 12.4% | 12.9% | 13.3% | 13.8% |  |
| EBIT (\$M) | 480 | 526 | 574 | 628 | 690 | 9.5% |
| EPS (\$) | 2.40 | 2.65 | 2.90 | 3.18 | 3.50 | 9.9% |
| Free cash flow (\$M) | 380 | 410 | 430 | 470 | 520 | 8.2% |
| FCF ÷ net income | 106% | 103% | 99% | 99% | 99% |  |

- **Operating leverage** turned 5.7% revenue growth into 9.5% EBIT growth: margins widened 1.8 points as fixed costs were spread over more sales.
- **EPS grew slightly faster than EBIT** because interest costs fell as debt was repaid; the share count was flat.
- **Cash backs the earnings:** free cash flow tracked net income (conversion near 100%), so the growth is real.
- **The valuation question:** can margins keep expanding? If they plateau near 14%, EPS growth slows toward revenue growth of about 6%. Never extrapolate 10% forever.

## 5.3 Quality of growth: eight tests

| Test | Good sign | Warning sign |
| --- | --- | --- |
| Organic | Most growth comes from the existing business | Growth mostly bought through acquisitions |
| Profitable | Margins stable or rising | Revenue up, margins down: growth bought with price cuts |
| Cash-backed | Free cash flow grows with earnings | Earnings up, cash flat as receivables or inventory build |
| Capital-efficient | High incremental ROIC (change in NOPAT ÷ change in invested capital) | Needs ever more capital per dollar of profit |
| Per share | EPS and FCF per share rising | Rising share count (dilution) |
| Diversified | Spread across customers, products and regions | One customer or product dominates |
| Repeatable | Recurring revenue, contracts, subscriptions | One-off orders or a cyclical peak |
| Not fully priced | The price implies less growth than you expect | The price assumes perfection (reverse DCF, [Module 6](06-equity-valuation.md)) |

## 5.4 What drives growth

- **Revenue = volume × price × mix.** Price-led growth shows pricing power unless it merely passes on inflation; volume-led growth shows real demand.
- **Customer businesses:** customers × retention × revenue per customer.
- **Market growth plus share gains:** a company gaining share in a market growing 3% can grow much faster than 3%.
- **Market sizing:** total addressable market (TAM), serviceable available market (SAM) and serviceable obtainable market (SOM). Be skeptical of giant TAM slides.
- **The adoption S-curve:** slow start, rapid growth, saturation. Mature companies grow roughly with the economy.
- **Base rates:** very few companies sustain growth above 20% a year for a decade. High growth fades toward the economy's rate, so your forecasts should fade too.

## 5.5 Sustainable and fundamental growth

```math
g_{sustainable} = ROE \times b \qquad g_{NOPAT} = \text{Reinvestment rate} \times ROIC
```

- **b** is the retention ratio, 1 − payout ratio.
- **Example:** ROE of 15% with a 40% payout leaves 60% retained, so the company can grow about 9% a year without new equity or more leverage.
- **Example:** a company reinvesting half its after-tax operating profit at a 12% ROIC grows operating profit about 6% a year.
- **The implication:** a company promising 15% growth with an 8% ROE and a 50% payout (sustainable growth of 4%) must borrow, issue shares or raise its returns. Ask which.

## 5.6 When growth creates value, and when it destroys it

```math
Value = \frac{NOPAT \times \left(1 - \frac{g}{ROIC}\right)}{WACC - g}
```

Take a company with \$100 million of NOPAT, an 8% WACC and 4% growth. With no growth it would be worth \$100M ÷ 8% = \$1,250M.

| Return on new investment (ROIC) | Value | Effect of growing 4% a year |
| --- | --- | --- |
| 15% | \$1,833M | Adds \$583M |
| 8% | \$1,250M | Adds nothing |
| 6% | \$833M | Destroys \$417M |

Growth helps only when ROIC exceeds WACC. A company earning below its cost of capital becomes less valuable the faster it grows. Economic profit, (ROIC − WACC) × invested capital, tracks this year by year.

## 5.7 Forecasting growth

- **Top-down:** market size × market share. **Bottom-up:** units × price, stores × sales per store, or customers × spend per customer.
- **Consensus estimates** are a reference point, not an answer. Explain where and why you differ.
- **Three cases:** build bear, base and bull forecasts, and fade growth toward about 4% nominal (roughly long-run nominal GDP growth) by year 10.
- **Sanity checks:** the implied market share, implied margins vs the best peers, and the capital the forecast requires.

## 5.8 Analyzing growth in ETFs, bonds, TIPS and other assets

| Asset | What "growth" means | How to analyze it |
| --- | --- | --- |
| Stock ETF | Growth in the earnings and dividends of its holdings, plus valuation change | Weighted EPS growth, dividend growth, P/E vs history, total return vs benchmark ([Module 8](08-etfs-funds-and-index-investing.md)) |
| Dividend ETF | Growth of the income stream | 5- and 10-year dividend growth, payout ratios of holdings, yield vs history |
| Bond or bond fund | No growth: the return is close to the starting yield over roughly its duration | Yield to maturity or SEC yield, duration, credit quality |
| TIPS | Principal grows with CPI; purchasing power grows at the real yield | Real yield at purchase, breakeven inflation, duration ([Module 7](07-fixed-income-and-tips.md)) |
| REIT | Growth in rents and cash flow | FFO and AFFO per share growth, same-store NOI growth, occupancy |
| Gold and commodities | No cash flows, so price change only | Real interest rates, the dollar, supply and demand, the futures curve |
| Fund assets under management | Popularity, not performance | Signals liquidity and the fund's survival, not future returns |

## 5.9 Step-by-step growth analysis checklist

1. Collect 5–10 years of revenue, gross profit, EBIT, EPS, free cash flow, dividends and share count.
2. Compute year-over-year growth and CAGRs for each line.
3. Split revenue growth into organic, acquired and currency effects.
4. Decompose it into volume, price and mix, or customers and revenue per customer.
5. Check margins: is operating leverage helping or hurting?
6. Check cash: free-cash-flow conversion and working-capital trends.
7. Compute ROIC and incremental ROIC, and compare them with WACC.
8. Check per-share growth and dilution.
9. Compare with peers and with industry growth.
10. Forecast three cases, fading growth over time.
11. Run a reverse DCF to see what growth the price implies ([Module 6](06-equity-valuation.md)).
12. Conclude: is the growth high-quality, durable and not yet priced in?

## Apply it to your case

- Show a 5-year growth table like Harbor Foods' for each stock in your report's appendix.
- For a conservative client, steady mid-single-digit growth with rising dividends and strong cash conversion beats fast but fragile growth. Say so explicitly in the IPS and in each stock thesis.

---

[← Module 4 · Financial statements and business analytics](04-financial-statements-and-business-analytics.md) · [Course contents](README.md) · [Module 6 · Equity valuation →](06-equity-valuation.md)
