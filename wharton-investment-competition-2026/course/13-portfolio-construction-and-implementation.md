# Module 13 · Portfolio construction and implementation

Implementation turns the allocation into actual holdings. Good implementation is cheap, diversified and tax-aware, and every position has a written reason for being there.

## 13.1 From allocation to holdings

- **Top-down:** macro view → asset allocation → sectors → securities. **Bottom-up:** start from great companies. Private banks usually combine the two: top-down allocation, bottom-up selection inside each sleeve.
- **For each sleeve, choose the vehicle:** an index fund, an active fund or individual securities. Use ETFs where you have no edge (bonds, international, the broad market) and individual stocks only where research adds conviction and diversification survives.

## 13.2 The security selection process

1. **Screen** for candidates with quantitative filters. A conservative-friendly screen: market cap above \$10 billion, ROE above 15%, net debt below 2× EBITDA, 10+ consecutive years of dividend increases, payout ratio below 60% and beta below 1.
2. **Research** business quality, financials and growth (Modules 3–5).
3. **Value** the company with at least two methods ([Module 6](06-equity-valuation.md)).
4. **Check risk:** how did it do in 2008, 2020 and 2022, and how does it correlate with what you already own?
5. **Write the thesis** (13.3).
6. **Size** the position (13.5) and set the sell criteria.
7. **Execute** with limit orders and record the trade in the log (13.9).

## 13.3 The one-page investment thesis

| Section | What to write |
| --- | --- |
| Recommendation | Buy, hold or sell; target weight; role, such as "defensive dividend grower" |
| The business | What it does, in one sentence |
| Thesis | Three reasons you expect it to do well |
| Valuation | Base, bull and bear values per share against the price; margin of safety |
| Catalysts | Events that could unlock value: earnings, launches, rate changes |
| Risks and mitigants | The top three risks and why they are acceptable |
| Sell criteria | What would prove you wrong: a dividend cut, margins below a set level, valuation above a set multiple |
| Client fit | How the holding serves the IPS: income, stability, inflation protection |

## 13.4 Sector analysis

The Global Industry Classification Standard (GICS) groups stocks into 11 sectors.

| Sector | Cyclical or defensive | Sensitivity to interest rates | Behavior with inflation | Dividends | Metrics to watch |
| --- | --- | --- | --- | --- | --- |
| Information Technology | Cyclical, growth | High (long-dated profits) | Mixed | Low to moderate | Revenue growth, gross margin, R&D |
| Communication Services | Mixed | Moderate | Mixed | Low to moderate | Users, revenue per user, advertising |
| Consumer Discretionary | Cyclical | Moderate | Hurt when real incomes fall | Low to moderate | Same-store sales, margins |
| Consumer Staples | Defensive | Moderate (partly bond-like) | Pricing power decides | High, steady | Volume vs price, margins |
| Health Care | Defensive | Low to moderate | Limited | Moderate | Pipeline, patents, policy |
| Financials | Cyclical | Banks gain from a steeper curve | Mixed | Moderate | Net interest margin, credit quality, capital |
| Industrials | Cyclical | Moderate | Mixed | Moderate | Orders, backlog, margins |
| Energy | Cyclical | Low | Tends to benefit | High but variable | Production, breakeven price, reserves |
| Materials | Cyclical | Low | Tends to benefit | Moderate | Commodity prices, costs |
| Utilities | Defensive | High (bond-like) | Regulated pass-through, with a lag | High | Rate-base growth, allowed return |
| Real Estate | Mixed | High | Partial hedge | High | FFO, occupancy, cap rates |

A conservative tilt usually favors consumer staples, health care, utilities and high-quality industrials. Because staples and utilities behave partly like bonds, they can lag when interest rates rise, so do not treat them as risk-free.

## 13.5 Position sizing

- **Equal weight** within a sleeve is simple and guards against overconfidence.
- **Conviction-weighted:** larger positions for higher conviction, within the IPS limits.
- **Risk-based (inverse volatility):** smaller weights for more volatile holdings, so each contributes similar risk.
- **IPS limits:** for example, no stock above 5% of the portfolio and no sector above 25% of the equity sleeve.
- **How many stocks?** Classic studies suggest 20–30 well-chosen stocks across sectors remove most company-specific risk in one market. With an index-fund core, a handful of individual satellites is fine.
- **Capital is not risk:** stocks can be a third of the capital and 80% of the risk (see the Appendix). Check each sleeve's contribution to total risk, not just its weight.

## 13.6 Trading and execution

- **Use limit orders,** especially for ETFs with wider spreads and in volatile markets. Avoid the first and last minutes of the trading day, when spreads are widest.
- **Transaction costs:** commissions (now near zero), the bid-ask spread, market impact and the cost of delay.
- **Scale in** over days or weeks if entry timing worries the client.
- **Dividend dates:** buying just before the ex-dividend date earns a taxable dividend that the price drop offsets. There is no free money.
- **In the simulator:** learn its order types, settlement and treatment of dividends and cash before you trade.

## 13.7 Rebalancing

- **Why:** without it, the riskiest assets grow to dominate the portfolio. Rebalancing mechanically sells high and buys low.
- **Methods:** calendar (quarterly or annual), threshold (for example ±5 points absolute, or ±20% of the target) or a hybrid that checks quarterly and acts on thresholds.
- **Example:** the target is 40% stocks and 60% bonds. After a rally the mix is 48/52. On a \$500,000 portfolio, sell \$40,000 of stocks and buy bonds to return to 40/60.
- **Keep costs down:** rebalance with new contributions, dividends and withdrawals first. In taxable accounts, sell lots with losses or the highest cost basis.

## 13.8 Tax management (US)

- **Asset location:** hold tax-inefficient assets (taxable bonds, TIPS, REITs, high-turnover funds) in tax-deferred accounts; tax-efficient ones (broad equity ETFs, municipal bonds) in taxable accounts; and the highest-growth assets in Roth accounts.
- **Holding period:** gains on assets held more than a year are long-term and taxed at 0%, 15% or 20% depending on income, plus a 3.8% net investment income tax for high earners. Short-term gains are taxed as ordinary income.
- **Qualified dividends** are taxed at long-term rates if the holding-period test is met.
- **Tax-loss harvesting:** sell losers to realize losses that offset gains, plus up to \$3,000 of ordinary income a year. The wash-sale rule disallows the loss if you buy a substantially identical security within 30 days before or after the sale.
- **Lot selection:** specific identification (for example, highest cost first) minimizes realized gains.
- **Giving and inheritance:** donating appreciated shares to charity avoids the gain, and under current law heirs receive a step-up in cost basis.

## 13.9 The trade log

Judges read your trading record, and the Trading Notes Analysis is due Oct 23, 2026. Log every trade the day you make it.

| Date | Ticker | Action | Shares | Price | Amount | Weight after | Reason | IPS link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Example | VTIP | Buy | 280 | \$50.00 | \$14,000 | 14% | Inflation protection for needs in the next 0–5 years with little rate risk | Risk objective; inflation concern |

## 13.10 Competition implementation tips

- Build the full portfolio early, so the IPS and final report describe a real, live portfolio.
- Do not over-trade. Every trade needs a reason tied to the IPS.
- Hold cash only where the IPS calls for it.
- Record each decision, its reason and the data behind it on the day you make it.
- Ten weeks of returns are mostly noise. Judges score the process, so manage for the client's 10-year goals, not the leaderboard.

## Apply it to your case

- Write a one-page thesis for each individual stock and a one-paragraph role statement for each fund.
- Size positions within the IPS limits and check each sleeve's contribution to total risk.
- Start the trade log now, and back-fill any trades made since the competition began on September 28.

---

[← Module 12 · Portfolio theory and asset allocation](12-portfolio-theory-and-asset-allocation.md) · [Course contents](README.md) · [Module 14 · Risk assessment and management →](14-risk-assessment-and-management.md)
