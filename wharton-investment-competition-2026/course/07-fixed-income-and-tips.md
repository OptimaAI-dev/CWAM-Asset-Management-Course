# Module 7 · Fixed income and TIPS

Bonds are the ballast of a conservative portfolio. Know exactly what can go wrong (rates, inflation, credit, liquidity), match maturities to the client's spending needs, and use TIPS to protect purchasing power.

## 7.1 Bond basics

```math
P = \sum_{t=1}^{n} \frac{C}{(1 + y)^{t}} + \frac{F}{(1 + y)^{n}}
```

- **Terms:** face (par) value F, coupon C, maturity n, price P and yield y.
- **Price and yield move in opposite directions.** When market rates rise, existing bonds with lower coupons are worth less.
- **Premium and discount:** a bond trades above par when its coupon exceeds market yields, and below par when it is lower.
- **Yield measures:** current yield = annual coupon ÷ price. Yield to maturity (YTM) is the discount rate that makes the present value of all cash flows equal the price; it is your return if you hold to maturity, nothing defaults and coupons are reinvested at the same yield. Yield to worst is the lowest of the YTM and the yields to each call date. Bond funds report a standardized SEC 30-day yield.
- **Clean and dirty price:** the dirty (invoice) price adds accrued interest to the quoted clean price.
- **Spot and forward rates:** spot rates are yields on zero-coupon bonds; forward rates are the future rates implied by today's curve.

## 7.2 Interest-rate risk: duration and convexity

```math
\frac{\Delta P}{P} \approx -D_{mod}\,\Delta y + \tfrac{1}{2}\,C\,(\Delta y)^{2}
```

- **Macaulay duration:** the weighted-average time, in years, until you receive the bond's cash flows.
- **Modified duration:** the approximate percentage price change for a 1-point change in yield.
- **Effective duration:** used for bonds with embedded options (callables, mortgages), measured by shocking yields up and down.
- **Convexity:** the curvature of the price-yield relationship. For ordinary bonds, prices rise more when yields fall than they drop when yields rise by the same amount.
- **DV01:** the dollar change in value for a 0.01-point (1 basis point) change in yield.

**Worked example.** A 10-year bond with a 4% annual coupon is priced to yield 5%.

- Price: \$922.78 per \$1,000 of face value, a discount because the coupon is below the yield.
- Macaulay duration 8.36 years, modified duration 7.96, convexity 78.3.
- If yields rise to 6%, the price falls to \$852.80, down 7.58%. Duration alone predicts −7.96%; adding convexity gives −7.57%, almost exact.
- If yields fall to 4%, the price rises to \$1,000.00, up 8.37%. The gain beats the loss for the same move: that is convexity.

Longer maturities and lower coupons mean higher duration, and a zero-coupon bond's duration equals its maturity. Rising rates hurt prices but let you reinvest coupons at higher yields; at roughly the duration horizon the two effects offset. That is the idea behind immunization: match the portfolio's duration to when the client needs the money.

## 7.3 Treasuries and yield-curve strategies

- **Bills** mature in 4, 6, 8, 13, 17, 26 or 52 weeks and are sold at a discount. **Notes** run 2, 3, 5, 7 or 10 years; **bonds** 20 or 30 years; **TIPS** 5, 10 or 30 years; floating-rate notes 2 years. STRIPS are zero-coupon pieces of Treasuries.
- Treasury interest is exempt from state and local income tax.
- **Ladder:** equal amounts maturing every year (for example years 1–5). It gives steady liquidity and averages out interest rates. It is the classic tool for a conservative client with known cash needs.
- **Bullet:** maturities clustered around one date, matched to a goal such as a down payment in year 3.
- **Barbell:** short and long maturities with nothing in the middle, for liquidity plus yield.
- **Riding the yield curve:** buy on the steep part of the curve; as the bond ages, its yield falls and its price rises.
- **Duration positioning:** shorten duration if you expect rates to rise, lengthen it if you expect them to fall.

## 7.4 Credit risk

| Grade | S&P and Fitch | Moody's | Meaning |
| --- | --- | --- | --- |
| Investment grade | AAA, AA, A, BBB | Aaa, Aa, A, Baa | Strong to adequate capacity to repay |
| High yield | BB, B | Ba, B | Speculative |
| Distressed | CCC to C, and D for default | Caa to C | Vulnerable or in default |

- **The cut-off:** BBB− (Baa3) is the lowest investment-grade rating. Bonds downgraded below it are "fallen angels" and often must be sold by funds restricted to investment grade.
- **Expected loss** = probability of default × loss given default (1 − recovery rate) × amount exposed.
- **Credit spread:** corporate yield minus the Treasury yield of the same maturity; the option-adjusted spread (OAS) handles bonds with options. Spreads widen in recessions, which is why corporate bonds fall when stocks fall.
- **Seniority:** senior secured debt is repaid first, then senior unsecured, subordinated debt, preferred stock and finally common equity.
- **Credit analysis:** capacity to pay (cash flow, interest coverage, debt to EBITDA), collateral, covenants and the character of management.

## 7.5 Other bond sectors

| Sector | What it is | Appeal | Main risks |
| --- | --- | --- | --- |
| Municipal bonds | State and local government debt | Interest free of federal tax, often of state tax for in-state buyers | Credit (especially revenue bonds), rates; pointless in tax-advantaged accounts |
| Agency mortgage-backed securities | Pools of home loans guaranteed by Ginnie Mae, Fannie Mae or Freddie Mac | Extra yield over Treasuries | Prepayments; negative convexity |
| Investment-grade corporates | Debt of strong companies | Spread over Treasuries | Spread widening in recessions |
| High-yield corporates | Debt of weaker companies | High coupons | Defaults; behave like stocks in a crisis |
| International and emerging-market bonds | Foreign government and corporate debt | Diversification; higher yields in emerging markets | Currency and political risk |
| CDs | Bank deposits with fixed terms | FDIC insurance up to \$250,000 per depositor, per insured bank, per ownership category | Penalties for early withdrawal |
| Money market funds | Pools of very short-term debt | Daily liquidity | Yield falls quickly when the Fed cuts |
| Preferred stock | A hybrid of bond and stock | Fixed dividends | Long duration, credit and call risk |
| Convertible bonds | Bonds that can convert into stock | Stock upside with a bond floor | Complexity, credit risk |

```math
\text{Taxable-equivalent yield} = \frac{\text{Municipal yield}}{1 - t}
```

A 3.5% municipal bond is worth a 5.15% taxable yield to an investor in the 32% federal bracket.

## 7.6 TIPS: inflation protection explained

**How they work**

- The principal is adjusted for inflation using CPI-U (not seasonally adjusted), with a lag of about three months.
- A fixed real coupon is paid every six months on the adjusted principal, so interest payments rise with inflation.
- At maturity you receive the inflation-adjusted principal or the original par, whichever is greater. That is the deflation floor.
- TIPS are issued with 5-, 10- and 30-year maturities, sold at auction and traded on the secondary market.

```math
\text{Adjusted principal} = \text{Par} \times \frac{CPI_{\text{today}}}{CPI_{\text{issue}}} \qquad \text{Interest} = \text{Real coupon} \times \text{Adjusted principal}
```

**Example.** Buy \$10,000 of TIPS with a 1.5% real coupon. CPI rises 3% over the year, so the principal becomes \$10,300 and the year's interest is about 1.5% × \$10,300 = \$154.50, paid in two halves. If CPI fell 2% instead, the principal would drop to \$9,800 along the way, but you would still get at least \$10,000 back at maturity.

**Real yield and breakeven inflation**

- TIPS are quoted by their real yield: the return above inflation if held to maturity.
- Breakeven inflation = nominal Treasury yield − TIPS real yield, at the same maturity. Illustration: a 10-year Treasury at 4.3% and a 10-year TIPS at 1.9% imply 2.4% breakeven. If inflation averages more than 2.4% over the decade, TIPS beat the nominal bond; if less, the nominal bond wins. Check current figures on Treasury's daily real yield curve.
- Breakevens also carry an inflation risk premium and get distorted when markets are stressed, so treat them as an imperfect forecast.

**Risks people miss**

- **Real-rate risk:** TIPS have duration. When real yields jumped in 2022, broad TIPS indexes lost roughly 12% even as inflation surged, while short-term TIPS lost only about 3% (approximate). TIPS protect against inflation, not against rising real rates, so match their maturity to the client's horizon.
- **Phantom income:** the yearly inflation adjustment to principal is taxable federal income even though you receive it only at maturity. Hold TIPS in tax-advantaged accounts, or use TIPS funds, which pay the adjustment out. TIPS income is exempt from state and local tax.
- **Deflation:** the floor protects only the original par at maturity. Inflation already accrued, or a price paid above par, can still be lost.
- **Liquidity:** the TIPS market is smaller than the nominal Treasury market, and trading costs widen in a crisis, as in late 2008.

**How to own TIPS**

- Individual TIPS at auction (through TreasuryDirect or a broker) or on the secondary market through a broker.
- **TIPS ladders:** buy TIPS maturing in each year you will need money, creating an inflation-protected income stream. A popular retirement-income tool.
- **TIPS funds and ETFs:** broad (all maturities) or short-term (0–5 years). Compare duration, expense ratio and SEC yield. Tickers to research: SCHP and TIP (broad), VTIP and STIP (short-term).

**When TIPS fit:** the client's goals are in real terms (living costs); you expect inflation above the breakeven rate or want insurance against it; or real yields are positive, so holding to maturity locks in a guaranteed real return.

**I bonds (Series I savings bonds)**

```math
\text{Composite rate} = r_{fixed} + 2\,\pi_{semi} + r_{fixed} \times \pi_{semi}
```

- Rates reset every May and November, based on CPI-U.
- Electronic purchases are capped at \$10,000 per person per calendar year; check TreasuryDirect for current rules.
- You must hold them 12 months, and redeeming before 5 years forfeits the last 3 months of interest.
- Interest is tax-deferred until redemption and exempt from state and local tax.
- Good for an individual's safe money, but they cannot be traded in a simulator.

## 7.7 Bond funds vs individual bonds

| Feature | Individual bonds | Bond funds and ETFs | Defined-maturity ETFs |
| --- | --- | --- | --- |
| Maturity | A fixed date when principal returns (absent default) | None: duration stays roughly constant | A fixed year, then cash is paid out |
| Price risk if held | Disappears at maturity | Persists | Fades as maturity approaches |
| Diversification | Needs many bonds for corporate credit | Hundreds of bonds | Many bonds |
| Costs | Dealer markups | Expense ratio, as low as about 0.03% | Expense ratio |
| Liquidity | Varies; poor for small lots | Daily | Daily |
| Best use | Ladders and specific goals | Core bond exposure | Goal-matched ladders in fund form (e.g., iShares iBonds, Invesco BulletShares) |

## 7.8 Checklist for any bond or bond fund

1. **Yield:** YTM or SEC yield, not the distribution yield.
2. **Duration:** how much will it fall if rates rise 1 point?
3. **Credit quality:** average rating and the share below investment grade.
4. **Concentration:** by sector and issuer.
5. **Inflation exposure:** nominal or inflation-linked?
6. **Costs:** expense ratio and bid-ask spread.
7. **Liquidity:** trading volume and fund size.
8. **Taxes:** federal, state, phantom income, tax-exempt status.
9. **Embedded options:** call risk and mortgage prepayments (negative convexity).
10. **Fit:** does the maturity match when the client needs the money?

## Apply it to your case

- Map each of Laura's cash needs to a T-bill or bond maturity. Money needed within about three years does not belong in long bonds or stocks.
- Set a duration target for the bond sleeve and justify it with your rate view and her horizon. For a risk-averse client, short-to-intermediate duration (roughly 2–5 years) is the usual default.
- Decide how much inflation protection she needs. Short-term TIPS answer the worry "I don't want inflation to eat my savings" directly.

---

[← Module 6 · Equity valuation](06-equity-valuation.md) · [Course contents](README.md) · [Module 8 · ETFs, funds and index investing →](08-etfs-funds-and-index-investing.md)
