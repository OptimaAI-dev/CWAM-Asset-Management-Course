# Module 1 · Investment foundations

Every investment decision trades off five things: return, risk, liquidity, time and taxes. From 1928 to 2023, US stocks compounded at 9.8% a year and 3-month T-bills at 3.3%. That gap is the reward for bearing risk, and this module shows how to measure both sides of it.

## 1.1 Time value of money

A dollar today is worth more than a dollar later because it can earn a return in the meantime. Bond pricing, valuation and retirement planning all come down to compounding forward or discounting back.

```math
FV = PV \times (1 + r)^{n} \qquad PV = \frac{FV}{(1 + r)^{n}}
```

- **Compounding:** \$100,000 invested at 5% for 10 years grows to \$162,889.
- **Rule of 72:** the years to double are roughly 72 ÷ the rate in percent. At 6% that gives 12 years; the exact answer is 11.9.
- **Inflation runs compounding in reverse:** after 10 years of 3% inflation, \$100,000 buys only what \$74,409 buys today.
- **Real vs nominal (Fisher):** the real return is what you earn in purchasing power.

```math
1 + r_{real} = \frac{1 + r_{nominal}}{1 + \pi} \qquad r_{real} \approx r_{nominal} - \pi
```

Example: a 6% nominal return with 3% inflation is a 2.91% real return (the shortcut gives 3%).

> **Banker's note:** State a conservative client's return goal in real terms. A 4% return feels safe, but with 2.5% inflation it adds only about 1.5% a year of purchasing power.

## 1.2 Measuring return

- **Holding period return (HPR):** (ending price − beginning price + income) ÷ beginning price.
- **Total return:** price change plus income (dividends, interest), with the income reinvested. Always compare assets on total return.
- **Arithmetic vs geometric mean:** the arithmetic average of yearly returns overstates what an investor actually earns when returns swing. The geometric mean, also called the compound annual growth rate (CAGR), is the true growth rate. A gain of 50% followed by a loss of 50% averages 0%, but \$100 becomes \$150 and then \$75, a geometric return of −13.4% a year.
- **Volatility drag:** the geometric mean is roughly the arithmetic mean minus half the variance. For the S&P 500 from 1928 to 2023, 11.66% arithmetic minus half of 19.55% squared (1.91 points) is close to the actual 9.80% geometric return.
- **Annualizing:** (1 + cumulative return) raised to the power 1 ÷ years, minus 1. Do not annualize periods shorter than a year in a client report, since it exaggerates.
- **Which return the client lives on:** nominal → after fees → after taxes → after inflation. Report the last one when you discuss goals.

## 1.3 Understanding risk

Risk is the chance that outcomes differ from what you expect: above all, the chance of losing money or missing a goal.

- **How to measure it:** standard deviation (volatility), maximum drawdown, worst year, probability of loss and probability of missing the goal (shortfall risk). [Module 14](14-risk-assessment-and-management.md) covers each.
- **Systematic vs unsystematic:** diversification removes company-specific (unsystematic) risk but not market-wide (systematic) risk. Markets pay a premium only for systematic risk (CAPM, [Module 12](12-portfolio-theory-and-asset-allocation.md)).
- **The record:** US asset classes, 1928–2023, before fees and taxes ([Damodaran Online](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histret.html)):

| Asset (US) | Compound annual return | Annual volatility | Worst year | Losing years (of 96) |
| --- | --- | --- | --- | --- |
| S&P 500 stocks, dividends reinvested | 9.80% | 19.55% | −43.84% (1931) | 26 |
| Baa-rated corporate bonds | 6.68% | 7.71% | −15.68% (1931) | 16 |
| 10-year Treasury bonds | 4.57% | 7.95% | −17.83% (2022) | 19 |
| 3-month Treasury bills | 3.30% | 3.01% | +0.03% (2014) | 0 |

Inflation averaged roughly 3% a year over this period (approximate), so T-bills barely kept pace while stocks multiplied purchasing power. Note 2022: 10-year Treasuries had their worst year in the dataset, losing almost as much as stocks (−17.8% vs −18.0%). Treasuries carry no default risk, but they carry plenty of interest-rate risk. Safe is not the same as riskless.

## 1.4 The asset classes

| Asset class | What you own | Where the return comes from | Main risks | Role for a conservative client |
| --- | --- | --- | --- | --- |
| Cash equivalents (T-bills, money market funds, CDs) | Very short-term loans to the government or banks | Interest | Inflation, falling rates on reinvestment | Liquidity reserve, near-term goals |
| Treasury bonds | Loans to the US government | Coupons and price changes | Interest-rate and inflation risk | Ballast in recessions and market crashes |
| TIPS and I bonds | Inflation-indexed government debt | Real yield plus a CPI adjustment | Real interest-rate risk | Protect purchasing power |
| Investment-grade corporate bonds | Loans to financially strong companies | Coupons above Treasuries (the credit spread) | Spread widening, interest rates | Extra income over Treasuries |
| High-yield (junk) bonds | Loans to weaker companies | High coupons | Default; behave like stocks in crises | Small or none |
| Municipal bonds | Loans to states and cities | Federally tax-exempt interest | Credit, interest rates | Income in high-bracket taxable accounts |
| US stocks | Ownership of US companies | Earnings growth, dividends, valuation changes | Bear markets, recessions | Long-term growth above inflation |
| International stocks (developed and emerging) | Ownership of non-US companies | Same, plus currency moves | Currency, political risk | Diversification, cheaper valuations |
| Real estate (REITs) | Income-producing property | Rents and property values | Interest rates, leverage | Income, partial inflation hedge |
| Commodities and gold | Raw materials, precious metal | Price changes (futures roll for commodities) | High volatility, no income | Small inflation or crisis hedge |
| Private equity, private credit, hedge funds | Illiquid or complex strategies | Manager skill, illiquidity premium | Lock-ups, fees, opacity | Rarely; very wealthy clients only |
| Digital assets | Crypto tokens | Price changes only | Extreme volatility, regulation | Generally none |

## 1.5 Investment vehicles

| Vehicle | How it trades | Typical annual cost | Tax efficiency | Best use |
| --- | --- | --- | --- | --- |
| Individual stocks | Intraday on exchanges | Near-zero commissions plus the bid-ask spread | High: you choose when to sell | Conviction ideas, satellite positions |
| Individual bonds | Over the counter through dealers | Dealer markup built into the price | You control timing | Known maturity dates, bond ladders |
| ETFs | Intraday on exchanges | From about 0.03% for broad index funds; more for niche funds | High, thanks to in-kind redemptions | Core building blocks |
| Mutual funds | Once a day at net asset value (NAV) | From about 0.03% (index) to 1%+ (active); some charge sales loads | Lower: can distribute capital gains | Retirement plans, active managers |
| Closed-end funds | Intraday, often at a premium or discount to NAV | Often 1%+ including leverage costs | Medium | Niche income strategies |
| Money market funds | At a stable \$1 NAV (government funds) | Low | Interest taxed as income | Cash management |
| Certificates of deposit (CDs) | Bank deposit; penalty for early withdrawal | No explicit fee | Interest taxed as income | FDIC-insured fixed rates |
| Annuities | Insurance contract | Near zero (simple fixed) to 2–3% (variable) | Tax-deferred growth | Guaranteed lifetime income ([Module 9](09-alternatives-and-real-assets.md)) |

## 1.6 How markets work

- **Primary vs secondary market:** companies and governments raise money in the primary market (IPOs, new bond issues); investors then trade with each other in the secondary market.
- **Exchanges and market makers:** the NYSE and Nasdaq match buyers and sellers. Market makers quote a bid (what they pay) and an ask (what they charge); the gap is the bid-ask spread, a hidden trading cost.
- **Order types:** a market order fills now at whatever price is available. A limit order fills only at your price or better. A stop order becomes a market order once a trigger price trades; a stop-limit becomes a limit order. Use limit orders for ETFs and thinly traded stocks.
- **Settlement:** US stock and ETF trades settle one business day after the trade (T+1).
- **Market capitalization:** share price × shares outstanding. Common conventions put large caps above \$10 billion and small caps below \$2 billion.
- **Indexes:** the S&P 500 (500 large US companies, weighted by market value), the Dow Jones Industrial Average (30 stocks, weighted by share price), the Russell 2000 (US small caps), MSCI EAFE (developed markets outside North America), MSCI ACWI (global stocks) and the Bloomberg US Aggregate (US investment-grade bonds).
- **Margin and short selling:** borrowing to invest magnifies losses, and a short sale can lose more than 100%. Neither belongs in a conservative mandate.
- **Efficient market hypothesis (EMH):** prices reflect past prices (weak form), all public information (semi-strong) or all information (strong). Whichever form you believe, beating the market after costs is hard, so every active bet needs a reason.

## 1.7 The five levers you control

You cannot control returns. You can control these five, and judges reward teams that show they used them deliberately:

1. **Asset allocation:** the mix of asset classes ([Module 12](12-portfolio-theory-and-asset-allocation.md)).
2. **Diversification:** across and within asset classes, regions and issuers.
3. **Costs:** fund fees, trading spreads and turnover.
4. **Taxes:** which account holds which asset, and how long you hold it ([Module 13](13-portfolio-construction-and-implementation.md)).
5. **Behavior:** a written plan, disciplined rebalancing and no panic selling.

## Apply it to your case

- List each of Laura's goals with its horizon in years.
- Inflate each goal to future dollars: goal in today's dollars × (1 + inflation)^years.
- Record every liquidity need: amount and date.
- Name the risks she fears most: losing money, inflation, or running out of money.
- Draft one sentence to refine in Modules 10–11: "Laura needs a real return of about X% a year without a calendar-year loss larger than Y%."

---

[← Start here](00-start-here.md) · [Course contents](README.md) · [Module 2 · Economics for investors →](02-economics-for-investors.md)
