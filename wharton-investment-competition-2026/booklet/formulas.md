# Formula Booklet

Wharton Investment Competition edition · Prepared by Carlos · October 6, 2026

## How to use this booklet

Every formula the competition is likely to need, grouped by topic, with each variable defined and a note on when to use it. Sections A to K hold the formulas; the [key-terms glossary](key-terms.md) decodes acronyms and jargon. Worked examples for most formulas are in the [course](../course/README.md).

- **Rates go in as decimals:** 5% is 0.05.
- **Periods match the rate:** use a monthly rate with monthly periods; formulas are annual unless stated.
- **Signs:** in spreadsheets, money paid out is negative and money received is positive.
- **Rules of thumb are labelled as such.** They are quick checks, not substitutes for the full formula.

### Notation key

| Symbol | Meaning |
| --- | --- |
| r | Rate of return, discount rate or interest rate per period |
| rₑ, r\_d | Cost of equity, cost of debt |
| r\_f | Risk-free rate (T-bill or Treasury yield) |
| E(R) | Expected return |
| R\_m, R\_b, R\_p | Return of the market, the benchmark, the portfolio |
| σ, σ² | Standard deviation (volatility), variance |
| ρ | Correlation coefficient, from −1 to +1 |
| Cov | Covariance |
| β | Beta: sensitivity to the market |
| α | Alpha: return beyond what risk explains |
| w | Portfolio weight |
| n, t | Number of periods; a given period |
| m | Compounding periods per year |
| g | Growth rate |
| π | Inflation rate |
| PV, FV | Present value, future value |
| PMT | Payment per period |
| C, F | Coupon payment, face (par) value of a bond |
| y | Yield to maturity |
| D | Dividend (in valuation) or duration (in bonds) |
| P | Price |
| E | Earnings (in valuation) or equity (in capital structure) |
| V | Firm value (D + E) or portfolio value |
| T | Tax rate (or time to expiry, in options) |
| b | Retention ratio = 1 − payout ratio |
| A | Risk-aversion coefficient |
| N(·) | Cumulative standard normal distribution |
| Δ | Change in |
| Σ, ∏ | Sum, product |
| ln, e | Natural logarithm, Euler's number (about 2.718) |

## A · Time value of money and returns

**A1 · Future and present value of a lump sum**

```math
FV = PV(1 + r)^{n} \qquad PV = \frac{FV}{(1 + r)^{n}}
```

**A2 · Compounding m times a year, and continuously**

```math
FV = PV\left(1 + \frac{r}{m}\right)^{mn} \qquad FV = PV\,e^{rn}
```

**A3 · Effective annual rate (EAR, also called APY)**

```math
EAR = \left(1 + \frac{r}{m}\right)^{m} - 1 \qquad EAR_{\text{continuous}} = e^{r} - 1
```

Use it to compare rates quoted with different compounding.

**A4 · Ordinary annuity (payments at the end of each period)**

```math
PV = PMT \times \frac{1 - (1 + r)^{-n}}{r} \qquad FV = PMT \times \frac{(1 + r)^{n} - 1}{r}
```

For an annuity due (payments at the start of each period), multiply either result by (1 + r).

**A5 · Perpetuity and growing perpetuity**

```math
PV = \frac{PMT}{r} \qquad PV = \frac{C_1}{r - g} \quad (r > g)
```

**A6 · Growing annuity**

```math
PV = \frac{C_1}{r - g}\left[1 - \left(\frac{1 + g}{1 + r}\right)^{n}\right]
```

Values a stream that rises every year, such as withdrawals raised for inflation.

**A7 · Loan or mortgage payment**

```math
PMT = PV \times \frac{r}{1 - (1 + r)^{-n}}
```

**A8 · Net present value and internal rate of return**

```math
NPV = \sum_{t=0}^{n} \frac{CF_t}{(1 + r)^{t}} \qquad 0 = \sum_{t=0}^{n} \frac{CF_t}{(1 + IRR)^{t}}
```

Accept a project when NPV > 0, or when its IRR exceeds the required return.

**A9 · Holding period return**

```math
HPR = \frac{P_1 - P_0 + D_1}{P_0}
```

**A10 · Arithmetic and geometric mean return**

```math
\bar{R} = \frac{1}{n}\sum_{t=1}^{n} R_t \qquad R_G = \left[\prod_{t=1}^{n}(1 + R_t)\right]^{1/n} - 1
```

Use the geometric mean (CAGR) for past multi-year performance and the arithmetic mean for a single period's expected return.

**A11 · Volatility drag**

```math
R_G \approx \bar{R} - \frac{\sigma^{2}}{2}
```

**A12 · CAGR and annualizing**

```math
CAGR = \left(\frac{V_{\text{end}}}{V_{\text{begin}}}\right)^{1/n} - 1 \qquad R_{\text{annual}} = (1 + R_{\text{period}})^{k} - 1
```

k is the number of periods per year (12 for monthly data). Do not annualize periods shorter than a year in client reports.

**A13 · Real return (Fisher)**

```math
r_{\text{real}} = \frac{1 + r_{\text{nominal}}}{1 + \pi} - 1 \approx r_{\text{nominal}} - \pi
```

**A14 · After-tax return on income taxed every year**

```math
r_{\text{after tax}} = r\,(1 - T)
```

Gains that are taxed only when you sell are handled in section I.

**A15 · Log (continuously compounded) return**

```math
r_{\log} = \ln\left(\frac{P_1}{P_0}\right) = \ln(1 + HPR)
```

Log returns add across periods; simple returns compound.

**A16 · Return on equity with leverage**

```math
R_E = R_A + \frac{D}{E}\,(R_A - r_d)
```

Borrowing magnifies gains when the asset return R\_A beats the borrowing cost r\_d, and magnifies losses when it does not.

**A17 · Gain needed to recover from a loss L**

```math
\text{Required gain} = \frac{1}{1 - L} - 1
```

A 20% loss needs a 25% gain, a 33% loss needs 50%, and a 50% loss needs 100%.

**A18 · Rule of 72 (rule of thumb)**

Years to double ≈ 72 ÷ the rate in percent (69.3 for continuous compounding). Years to triple ≈ 114 ÷ the rate; to quadruple ≈ 144 ÷ the rate.

Time-weighted and money-weighted returns are in section D.

## B · Risk and portfolio statistics

**B1 · Variance and standard deviation**

```math
s^{2} = \frac{\sum_{t=1}^{n}(R_t - \bar{R})^{2}}{n - 1} \qquad s = \sqrt{s^{2}}
```

Use n − 1 for a sample of returns (STDEV.S) and n for a whole population (STDEV.P).

**B2 · Annualizing volatility**

```math
\sigma_{\text{annual}} = \sigma_{\text{period}} \times \sqrt{k}
```

k = 12 for monthly data, 52 for weekly, about 252 for daily. Mean returns scale with k; volatility scales with √k.

**B3 · Covariance and correlation**

```math
Cov(X, Y) = \frac{\sum (X_t - \bar{X})(Y_t - \bar{Y})}{n - 1} \qquad \rho_{XY} = \frac{Cov(X, Y)}{\sigma_X\,\sigma_Y}
```

**B4 · Beta**

```math
\beta_i = \frac{Cov(R_i, R_m)}{\sigma_m^{2}} = \rho_{im}\,\frac{\sigma_i}{\sigma_m}
```

Beta is also the slope of a regression of the asset's returns on the market's (SLOPE in a spreadsheet).

**B5 · Two-asset portfolio**

```math
E(R_p) = w_1 E(R_1) + w_2 E(R_2) \qquad \sigma_p^{2} = w_1^{2}\sigma_1^{2} + w_2^{2}\sigma_2^{2} + 2 w_1 w_2 \rho_{12}\sigma_1\sigma_2
```

**B6 · Portfolio of n assets (matrix form)**

```math
\sigma_p^{2} = \sum_{i=1}^{n}\sum_{j=1}^{n} w_i w_j\,Cov_{ij} = \mathbf{w}^{\top}\Sigma\,\mathbf{w}
```

Σ is the covariance matrix. Section K shows the spreadsheet version.

**B7 · Portfolio beta**

```math
\beta_p = \sum_{i=1}^{n} w_i\,\beta_i
```

**B8 · Equally weighted portfolio: why diversification has a floor**

```math
\sigma_p^{2} = \frac{1}{n}\,\overline{\sigma^{2}} + \left(1 - \frac{1}{n}\right)\overline{Cov}
```

As n grows, the first term vanishes, leaving the average covariance: market risk cannot be diversified away.

**B9 · Coefficient of variation**

```math
CV = \frac{\sigma}{\bar{R}}
```

Risk per unit of return; lower is better.

**B10 · Downside deviation (target T)**

```math
\sigma_{\text{down}} = \sqrt{\frac{1}{n}\sum_{t=1}^{n}\min(R_t - T,\,0)^{2}}
```

Counts only returns below the target; used in the Sortino ratio.

**B11 · Skewness and excess kurtosis**

```math
\text{Skew} = \frac{1}{n}\sum\left(\frac{R_t - \bar{R}}{\sigma}\right)^{3} \qquad \text{Excess kurtosis} = \frac{1}{n}\sum\left(\frac{R_t - \bar{R}}{\sigma}\right)^{4} - 3
```

Negative skew means occasional large losses; positive excess kurtosis means fat tails, so extreme moves happen more often than a bell curve predicts.

**B12 · Z-score and the normal distribution**

```math
z = \frac{x - \mu}{\sigma}
```

| Range around the mean | Share of outcomes inside (normal distribution) |
| --- | --- |
| ±1 σ | 68.3% |
| ±1.645 σ | 90% (5% in each tail) |
| ±1.96 σ | 95% |
| ±2.33 σ | 98% (1% in each tail) |
| ±2.58 σ | 99% |

**B13 · Confidence interval for a mean**

```math
\bar{x} \pm z \times \frac{s}{\sqrt{n}}
```

**B14 · Maximum drawdown**

```math
MDD = \max_{t}\left(\frac{\text{Peak before } t - V_t}{\text{Peak before } t}\right)
```

The largest peak-to-trough fall over the period.

**B15 · Parametric value at risk (VaR)**

```math
VaR_{\alpha} = (z_{\alpha}\,\sigma - \mu) \times V \qquad VaR_{h\text{ periods}} = (z_{\alpha}\,\sigma\sqrt{h} - \mu h) \times V
```

z = 1.645 for 95% and 2.33 for 99% confidence. VaR is the loss not exceeded with that confidence; it says nothing about the size of losses beyond it.

**B16 · Conditional VaR (expected shortfall), normal distribution**

```math
ES_{\alpha} = \left(\sigma\,\frac{\varphi(z_{\alpha})}{1 - \alpha} - \mu\right) \times V
```

φ is the standard normal density. At 95% confidence, φ(1.645) ÷ 0.05 ≈ 2.06, so ES ≈ (2.06σ − μ) × V. It is the average loss in the worst 5% of cases.

**B17 · Roy's safety-first ratio**

```math
SFR = \frac{E(R_p) - R_L}{\sigma_p} \qquad P(R_p < R_L) \approx N(-SFR)
```

R\_L is the minimum acceptable return. Choose the portfolio with the highest SFR to minimize the chance of falling short.

**B18 · Tracking error and R²**

```math
TE = \sigma(R_p - R_b) \qquad R^{2} = \rho^{2} \;\text{(one-factor regression)}
```

R² is the share of a fund's return variance explained by its benchmark or factors.

**B19 · Concentration: Herfindahl–Hirschman index**

```math
HHI = \sum_{i=1}^{n} w_i^{2} \qquad N_{\text{effective}} = \frac{1}{HHI}
```

Twenty equal positions give HHI = 0.05, the same as 20 effective holdings. Uneven weights reduce the effective number.

**B20 · Risk contribution**

```math
MCR_i = \frac{(\Sigma\mathbf{w})_i}{\sigma_p} \qquad RC_i = w_i \times MCR_i \qquad \sum_i RC_i = \sigma_p
```

RC\_i ÷ σ\_p is each holding's percentage share of total risk. A sleeve can hold a third of the money and most of the risk.

**B21 · Diversification ratio**

```math
DR = \frac{\sum_i w_i\,\sigma_i}{\sigma_p}
```

Above 1 means diversification is reducing risk; higher is more diversified.

**B22 · Linear regression (single factor)**

```math
R_{i,t} = \alpha + \beta R_{m,t} + \varepsilon_t \qquad \beta = \frac{Cov(R_i, R_m)}{Var(R_m)} \qquad \alpha = \bar{R}_i - \beta\,\bar{R}_m
```

The t-statistic of a coefficient is the estimate ÷ its standard error; above about 2 is usually treated as statistically significant.

## C · Portfolio theory, CAPM and factor models

**C1 · Minimum-variance weight for two assets**

```math
w_1^{*} = \frac{\sigma_2^{2} - \rho_{12}\sigma_1\sigma_2}{\sigma_1^{2} + \sigma_2^{2} - 2\rho_{12}\sigma_1\sigma_2} \qquad w_2^{*} = 1 - w_1^{*}
```

**C2 · Capital allocation line (risky portfolio P plus the risk-free asset)**

```math
E(R_C) = r_f + y\left[E(R_P) - r_f\right] \qquad \sigma_C = y\,\sigma_P
```

y is the share in the risky portfolio. The line's slope is P's Sharpe ratio, and the tangency portfolio maximizes it.

**C3 · Investor utility and the optimal risky share**

```math
U = E(r) - \tfrac{1}{2}A\sigma^{2} \qquad y^{*} = \frac{E(R_P) - r_f}{A\,\sigma_P^{2}}
```

A higher risk-aversion coefficient A means a smaller risky share. Typical values of A run from about 2 (tolerant) to 6 or more (very averse).

**C4 · Capital market line**

```math
E(R_p) = r_f + \frac{E(R_m) - r_f}{\sigma_m}\,\sigma_p
```

For efficient portfolios only; uses total risk σ.

**C5 · CAPM and the security market line**

```math
E(R_i) = r_f + \beta_i\left[E(R_m) - r_f\right]
```

For any asset; uses systematic risk β. E(R\_m) − r\_f is the market risk premium.

**C6 · Jensen's alpha**

```math
\alpha_p = R_p - \left[r_f + \beta_p (R_m - r_f)\right]
```

**C7 · Single-index model: total risk split in two**

```math
\sigma_i^{2} = \beta_i^{2}\sigma_m^{2} + \sigma^{2}(\varepsilon_i)
```

Systematic risk plus firm-specific risk. Only the first is rewarded, because diversification removes the second.

**C8 · Fama–French and Carhart factor models**

```math
R_i - r_f = \alpha_i + \beta_i(R_m - r_f) + s_i\,SMB + h_i\,HML + m_i\,UMD + \varepsilon_i
```

The three-factor model uses market, size (SMB) and value (HML). Carhart adds momentum (UMD). The five-factor model replaces momentum with profitability (RMW) and investment (CMA).

**C9 · Arbitrage pricing theory**

```math
E(R_i) = r_f + \beta_{i1}\lambda_1 + \beta_{i2}\lambda_2 + \cdots + \beta_{ik}\lambda_k
```

λ\_k is the risk premium for factor k, such as unexpected inflation or GDP growth.

**C10 · Grinold–Kroner expected stock return**

```math
E(R) \approx \frac{D}{P} + i + g - \Delta S + \Delta\frac{P}{E}
```

Dividend yield + expected inflation i + real earnings growth g − the yearly change in shares outstanding (buybacks make ΔS negative and add to return) + the yearly change in the P/E ratio.

**C11 · Building-block expected bond return**

```math
E(R_{bond}) \approx y_0 - \text{expected credit losses} \pm \text{roll-down and rate changes}
```

For high-quality bonds, today's yield is the best single estimate of the next 5–10 years' return.

**C12 · Implied equilibrium returns (Black–Litterman starting point)**

```math
\Pi = \lambda\,\Sigma\,\mathbf{w}_{mkt} \qquad \lambda = \frac{E(R_m) - r_f}{\sigma_m^{2}}
```

The returns that make market-cap weights optimal. Black–Litterman then blends in your views, weighted by your confidence.

**C13 · Inverse-volatility (naive risk parity) weights**

```math
w_i = \frac{1/\sigma_i}{\sum_{j}1/\sigma_j}
```

Full risk parity equalizes each asset's risk contribution (B20) instead: RC\_i = σ\_p ÷ n.

**C14 · Fundamental law of active management**

```math
IR \approx IC \times \sqrt{BR}
```

The information ratio depends on skill (information coefficient IC, the correlation between forecasts and outcomes) and breadth (BR, the number of independent bets per year).

## D · Risk-adjusted performance and attribution

**D1 · Sharpe ratio**

```math
S_p = \frac{R_p - r_f}{\sigma_p}
```

Excess return per unit of total risk. For reference, US stocks from 1928 to 2023 scored about 0.43 on annual data (average excess return over T-bills of 8.3 points ÷ 19.6% volatility).

**D2 · Sortino ratio**

```math
\text{Sortino} = \frac{R_p - T}{\sigma_{\text{down}}}
```

Like Sharpe, but penalizes only volatility below the target T (B10). It suits loss-averse clients.

**D3 · Treynor ratio**

```math
T_p = \frac{R_p - r_f}{\beta_p}
```

Excess return per unit of market risk. Use it for a sleeve that sits inside a diversified portfolio.

**D4 · Information ratio**

```math
IR = \frac{R_p - R_b}{\sigma(R_p - R_b)} = \frac{\text{Active return}}{\text{Tracking error}}
```

Skill relative to a benchmark. Above 0.5 sustained over years is strong.

**D5 · M² (Modigliani risk-adjusted performance)**

```math
M^{2} = r_f + S_p\,\sigma_b \qquad M^{2}\text{ excess} = M^{2} - R_b
```

The return the portfolio would have earned at the benchmark's volatility, in percent.

**D6 · Calmar ratio**

```math
\text{Calmar} = \frac{\text{Annualized return}}{|\text{Maximum drawdown}|}
```

**D7 · Upside and downside capture**

```math
\text{Up capture} = \frac{R_p \text{ in up periods}}{R_b \text{ in up periods}} \qquad \text{Down capture} = \frac{R_p \text{ in down periods}}{R_b \text{ in down periods}}
```

A conservative client wants down capture well below 100%. Capture ratio = up ÷ down; above 1 is good.

**D8 · Active return and active share**

```math
\text{Active return} = R_p - R_b \qquad \text{Active share} = \tfrac{1}{2}\sum_{i}\left|w_{p,i} - w_{b,i}\right|
```

Active share runs from 0% (an index fund) to 100% (no overlap with the benchmark).

**D9 · Time-weighted return**

```math
TWR = \left[\prod_{i=1}^{n}(1 + r_i)\right]^{1/\text{years}} - 1 \qquad r_i = \frac{V_{\text{end},i} - V_{\text{begin},i}}{V_{\text{begin},i}}
```

Split the period at every external cash flow; each sub-period's beginning value includes that flow. It removes the effect of the client's deposit timing and measures the manager.

**D10 · Modified Dietz return (approximate TWR for one period)**

```math
R = \frac{EMV - BMV - \sum CF_i}{BMV + \sum w_i\,CF_i} \qquad w_i = \frac{\text{days remaining after flow } i}{\text{days in period}}
```

**D11 · Money-weighted return**

```math
\sum_{t=0}^{n}\frac{CF_t}{(1 + MWR)^{t}} = 0
```

The IRR of all deposits, withdrawals and the ending value (XIRR in a spreadsheet). It measures the client's own experience.

**D12 · Brinson attribution (segment i)**

```math
\text{Allocation}_i = (w_{p,i} - w_{b,i})\,R_{b,i} \qquad \text{Selection}_i = w_{b,i}\,(R_{p,i} - R_{b,i}) \qquad \text{Interaction}_i = (w_{p,i} - w_{b,i})(R_{p,i} - R_{b,i})
```

The three effects summed over all segments equal R\_p − R\_b. The Brinson–Fachler variant measures allocation against the total benchmark return:

```math
\text{Allocation}_i^{BF} = (w_{p,i} - w_{b,i})(R_{b,i} - R_b)
```

**D13 · Linking returns across periods**

```math
R_{\text{cumulative}} = (1 + R_1)(1 + R_2)\cdots(1 + R_n) - 1
```

**D14 · Fee drag over n years**

```math
\frac{FV_{\text{after fees}}}{FV_{\text{before fees}}} = \left(\frac{1 + r - f}{1 + r}\right)^{n}
```

At 6% gross, a 1% fee leaves about 75% of the ending wealth after 30 years.

**D15 · Hit rate (batting average)**

```math
\text{Hit rate} = \frac{\text{Periods beating the benchmark}}{\text{Total periods}}
```

## E · Bonds, yields, duration and TIPS

**E1 · Bond price**

```math
P = \sum_{t=1}^{n}\frac{C}{(1 + y)^{t}} + \frac{F}{(1 + y)^{n}} \qquad \text{semiannual: } C \to \tfrac{C}{2},\; y \to \tfrac{y}{2},\; n \to 2n
```

**E2 · Zero-coupon bond**

```math
P = \frac{F}{(1 + y)^{n}} \qquad y = \left(\frac{F}{P}\right)^{1/n} - 1
```

**E3 · Current yield and approximate yield to maturity**

```math
\text{Current yield} = \frac{C}{P} \qquad YTM \approx \frac{C + (F - P)/n}{(F + P)/2}
```

The exact YTM solves E1 for y (YIELD or RATE in a spreadsheet). Yield to call uses the call date and call price instead of maturity and par; yield to worst is the lowest of them.

**E4 · Bond-equivalent and effective annual yield**

```math
BEY = 2 \times y_{\text{semiannual}} \qquad EAY = \left(1 + \frac{BEY}{2}\right)^{2} - 1
```

**E5 · Treasury bill yields (t = days to maturity)**

```math
\text{Discount yield} = \frac{F - P}{F} \times \frac{360}{t} \qquad \text{Investment (BEY) yield} = \frac{F - P}{P} \times \frac{365}{t}
```

Bills are quoted on the discount basis; the investment yield is the better comparison with other bonds.

**E6 · Accrued interest and dirty price**

```math
AI = \frac{C}{m} \times \frac{\text{days since last coupon}}{\text{days in coupon period}} \qquad \text{Dirty price} = \text{Clean price} + AI
```

**E7 · Spot and forward rates**

```math
(1 + s_n)^{n} = (1 + s_m)^{m}\,(1 + f_{m,n-m})^{n-m}
```

Example: (1 + s₂)² = (1 + s₁)(1 + f₁,₁). The forward rate f is the rate the curve implies for the future period.

**E8 · Macaulay and modified duration**

```math
D_{Mac} = \frac{1}{P}\sum_{t=1}^{n}\frac{t \times CF_t}{(1 + y)^{t}} \qquad D_{Mod} = \frac{D_{Mac}}{1 + y/m}
```

A zero-coupon bond's Macaulay duration equals its maturity; a perpetuity's is (1 + y) ÷ y.

**E9 · Effective duration and convexity (for bonds with options)**

```math
D_{Eff} = \frac{P_{-} - P_{+}}{2\,P_0\,\Delta y} \qquad C_{Eff} = \frac{P_{-} + P_{+} - 2P_0}{P_0\,(\Delta y)^{2}}
```

P₋ and P₊ are the prices after yields fall and rise by Δy.

**E10 · Price change from a yield change**

```math
\frac{\Delta P}{P} \approx -D_{Mod}\,\Delta y + \tfrac{1}{2}\,C\,(\Delta y)^{2}
```

Rule of thumb: a 1-point rise in yields cuts a bond's price by about its duration in percent.

**E11 · DV01 and portfolio duration**

```math
DV01 = D_{Mod} \times P \times 0.0001 \qquad D_{p} = \sum_i w_i\,D_i
```

DV01 (or PV01) is the dollar change in value for a 1-basis-point move in yield.

**E12 · Expected return on a bond over a horizon**

```math
E(R) \approx y + \text{roll-down} - D_{Mod}\,\Delta y + \tfrac{1}{2}C(\Delta y)^{2} - \text{credit losses} \pm \text{currency}
```

**E13 · Credit risk**

```math
EL = PD \times LGD \times EAD \qquad LGD = 1 - \text{recovery rate} \qquad \text{Spread} \approx PD \times LGD
```

Expected loss from the probability of default (PD), the loss given default (LGD) and the exposure at default (EAD). The spread approximation gives the annual compensation needed just to cover expected losses.

**E14 · Taxable-equivalent yield**

```math
TEY = \frac{y_{muni}}{1 - t} \qquad t_{\text{combined}} \approx t_{\text{federal}} + t_{\text{state}}
```

Use the combined rate for an in-state bond that is exempt from both federal and state tax.

**E15 · TIPS mechanics**

```math
\text{Index ratio} = \frac{CPI_{\text{ref, today}}}{CPI_{\text{ref, issue}}} \qquad \text{Adjusted principal} = \text{Par} \times \text{Index ratio}
```

```math
\text{Interest payment} = \frac{\text{Real coupon}}{2} \times \text{Adjusted principal} \qquad \text{Paid at maturity} = \max(\text{Adjusted principal},\ \text{Par})
```

**E16 · Breakeven inflation**

```math
\pi_{BE} = y_{\text{nominal}} - y_{\text{real}} \qquad \text{exact: } \pi_{BE} = \frac{1 + y_{\text{nominal}}}{1 + y_{\text{real}}} - 1
```

If realized inflation beats the breakeven rate, TIPS outperform nominal Treasuries of the same maturity.

**E17 · I bond composite rate**

```math
r_{\text{composite}} = r_{\text{fixed}} + 2\,\pi_{\text{semiannual}} + r_{\text{fixed}} \times \pi_{\text{semiannual}}
```

**E18 · Bond holding period return**

```math
HPR = \frac{P_1 - P_0 + C}{P_0}
```

**E19 · Bond-fund horizon (rule of thumb)**

A bond fund kept at a constant duration tends to return close to its starting yield over a horizon of roughly 2 × duration − 1 years, because higher reinvestment rates slowly offset the price loss from rising rates.

## F · Equity valuation: DCF, DDM, WACC, multiples

**F1 · Gordon growth dividend discount model**

```math
P_0 = \frac{D_1}{r - g} = \frac{D_0(1 + g)}{r - g} \qquad r = \frac{D_1}{P_0} + g \qquad g_{\text{implied}} = r - \frac{D_1}{P_0}
```

Valid only when r > g and growth is stable forever.

**F2 · Two-stage dividend discount model**

```math
P_0 = \sum_{t=1}^{n}\frac{D_t}{(1 + r)^{t}} + \frac{1}{(1 + r)^{n}} \times \frac{D_{n+1}}{r - g_L}
```

High growth for n years, then long-run growth g\_L.

**F3 · H-model (growth fading in a straight line)**

```math
P_0 = \frac{D_0(1 + g_L)}{r - g_L} + \frac{D_0\,H\,(g_S - g_L)}{r - g_L}
```

g\_S is today's short-term growth, g\_L the long-run rate, and H half the length of the fade period in years.

**F4 · Present value of growth opportunities**

```math
P_0 = \frac{E_1}{r} + PVGO
```

The price of a no-growth firm plus the value the market places on future growth.

**F5 · Free cash flow to the firm (FCFF)**

```math
FCFF = EBIT(1 - T) + D\&A - \text{Capex} - \Delta NWC = CFO + \text{Interest}(1 - T) - \text{Capex}
```

**F6 · Free cash flow to equity (FCFE)**

```math
FCFE = FCFF - \text{Interest}(1 - T) + \text{Net borrowing} = CFO - \text{Capex} + \text{Net borrowing}
```

Discount FCFF at WACC to get firm value; discount FCFE at the cost of equity to get equity value. Never mix them.

**F7 · DCF value and terminal value**

```math
V_0 = \sum_{t=1}^{n}\frac{FCFF_t}{(1 + WACC)^{t}} + \frac{TV_n}{(1 + WACC)^{n}} \qquad TV_n = \frac{FCFF_{n}(1 + g)}{WACC - g} \;\text{ or }\; TV_n = \text{Multiple} \times \text{Metric}_n
```

**F8 · Enterprise value and the bridge to equity**

```math
EV = \text{Market cap} + \text{Debt} + \text{Preferred} + \text{Minority interest} - \text{Cash}
```

```math
\text{Value per share} = \frac{EV - \text{Net debt} - \text{Preferred} - \text{Minority interest}}{\text{Diluted shares}}
```

**F9 · Weighted average cost of capital**

```math
WACC = \frac{E}{V}\,r_e + \frac{D}{V}\,r_d\,(1 - T) + \frac{P}{V}\,r_p
```

Use market-value weights; P is preferred stock.

**F10 · Cost of equity**

```math
r_e = r_f + \beta\,(ERP) \qquad r_e = r_f + ERP + \text{size premium} + \text{specific-risk premium}
```

CAPM, then the build-up method used for small or private companies. A quick cross-check: the company's bond yield plus 3–5 points (rule of thumb).

**F11 · Levering and unlevering beta (Hamada) and adjusted beta (Blume)**

```math
\beta_L = \beta_U\left[1 + (1 - T)\frac{D}{E}\right] \qquad \beta_{\text{adjusted}} = \tfrac{2}{3}\,\beta_{\text{raw}} + \tfrac{1}{3}
```

Unlever peers' betas, average them, then relever at your company's debt-to-equity ratio.

**F12 · Justified multiples from fundamentals**

```math
\frac{P_0}{E_1} = \frac{1 - b}{r - g} \qquad \frac{P_0}{E_0} = \frac{(1 - b)(1 + g)}{r - g} \qquad \frac{P_0}{B_0} = \frac{ROE - g}{r - g} \qquad \frac{P_0}{S_0} = \frac{PM\,(1 - b)(1 + g)}{r - g}
```

b is the retention ratio and PM the net profit margin. A company whose ROE equals its cost of equity deserves a P/B of 1.

**F13 · Other multiples and yields**

```math
PEG = \frac{P/E}{g \times 100} \qquad \text{Earnings yield} = \frac{E}{P} \qquad \text{FCF yield} = \frac{FCF}{\text{Market cap}} \qquad \text{Shareholder yield} = \frac{\text{Dividends} + \text{Net buybacks}}{\text{Market cap}}
```

**F14 · Residual income model**

```math
RI_t = E_t - r\,B_{t-1} = (ROE_t - r)\,B_{t-1} \qquad V_0 = B_0 + \sum_{t=1}^{\infty}\frac{RI_t}{(1 + r)^{t}}
```

**F15 · NOPAT, economic profit and EVA**

```math
NOPAT = EBIT(1 - T) \qquad EVA = NOPAT - WACC \times IC = (ROIC - WACC) \times IC
```

IC is invested capital (debt + equity − cash).

**F16 · Value driver formula**

```math
V_0 = \frac{NOPAT_1\left(1 - \frac{g}{RONIC}\right)}{WACC - g}
```

RONIC is the return on new invested capital. Growth adds value only when RONIC > WACC.

**F17 · Sustainable growth**

```math
g = ROE \times b \qquad g_{NOPAT} = \text{Reinvestment rate} \times ROIC
```

**F18 · Margin of safety and upside**

```math
\text{Margin of safety} = \frac{V - P}{V} \qquad \text{Upside} = \frac{V}{P} - 1
```

**F19 · Graham number (rule of thumb)**

```math
V_{Graham} = \sqrt{22.5 \times EPS \times BVPS}
```

Benjamin Graham's ceiling for a defensive investor: a P/E of 15 times a P/B of 1.5. A crude screen, not a valuation.

## G · Financial ratios and business analytics

Average balance-sheet figures (beginning + end ÷ 2) are preferred when a ratio divides a flow by a stock. Compare every ratio with the company's own history and with peers.

### G1 · Profitability

| Ratio | Formula |
| --- | --- |
| Gross margin | Gross profit ÷ revenue |
| Operating (EBIT) margin | EBIT ÷ revenue |
| EBITDA margin | EBITDA ÷ revenue |
| Net margin | Net income ÷ revenue |
| Return on assets (ROA) | Net income ÷ average total assets |
| Return on equity (ROE) | Net income ÷ average shareholders' equity |
| Return on invested capital (ROIC) | NOPAT ÷ average invested capital (debt + equity − cash) |
| Incremental ROIC | Change in NOPAT ÷ change in invested capital |

### G2 · Efficiency and working capital

| Ratio | Formula |
| --- | --- |
| Asset turnover | Revenue ÷ average total assets |
| Inventory turnover | Cost of goods sold ÷ average inventory |
| Days inventory outstanding (DIO) | 365 ÷ inventory turnover |
| Receivables turnover | Revenue ÷ average receivables |
| Days sales outstanding (DSO) | 365 ÷ receivables turnover |
| Payables turnover | Cost of goods sold ÷ average payables |
| Days payables outstanding (DPO) | 365 ÷ payables turnover |
| Cash conversion cycle | DIO + DSO − DPO |

### G3 · Liquidity

| Ratio | Formula |
| --- | --- |
| Current ratio | Current assets ÷ current liabilities |
| Quick (acid-test) ratio | (Cash + marketable securities + receivables) ÷ current liabilities |
| Cash ratio | (Cash + marketable securities) ÷ current liabilities |

### G4 · Leverage and coverage

| Ratio | Formula |
| --- | --- |
| Debt to equity | Total debt ÷ total equity |
| Debt to capital | Total debt ÷ (debt + equity) |
| Net debt to EBITDA | (Debt − cash) ÷ EBITDA |
| Equity multiplier | Average total assets ÷ average equity |
| Interest coverage | EBIT ÷ interest expense |
| Fixed-charge coverage | (EBIT + lease payments) ÷ (interest + lease payments) |
| FFO to debt (credit analysts) | Funds from operations ÷ total debt |

### G5 · Cash flow and payout

| Ratio | Formula |
| --- | --- |
| Free cash flow | Operating cash flow − capital expenditure |
| FCF margin | FCF ÷ revenue |
| FCF conversion | FCF ÷ net income |
| Accruals ratio | (Net income − operating cash flow) ÷ average total assets |
| Capex intensity | Capex ÷ revenue; capex ÷ depreciation above 1 signals growth investment |
| Payout ratio | Dividends ÷ net income (or ÷ FCF) |
| Retention ratio (b) | 1 − payout ratio |
| Dividend coverage | Net income (or FCF) ÷ dividends |
| Reinvestment rate | (Capex − D&A + increase in NWC) ÷ NOPAT |

### G6 · Per share

| Measure | Formula |
| --- | --- |
| Diluted EPS | (Net income − preferred dividends) ÷ diluted weighted-average shares |
| Book value per share | Common equity ÷ shares outstanding |
| Dividends per share | Total common dividends ÷ shares outstanding |
| FCF per share | FCF ÷ diluted shares |

### G7 · DuPont analysis

```math
ROE = \underbrace{\frac{NI}{Sales}}_{\text{margin}} \times \underbrace{\frac{Sales}{Assets}}_{\text{turnover}} \times \underbrace{\frac{Assets}{Equity}}_{\text{leverage}}
```

```math
ROE = \frac{NI}{EBT} \times \frac{EBT}{EBIT} \times \frac{EBIT}{Sales} \times \frac{Sales}{Assets} \times \frac{Assets}{Equity}
```

The five-step version adds the tax burden (NI ÷ EBT) and the interest burden (EBT ÷ EBIT).

### G8 · Operating, financial and total leverage

```math
DOL = \frac{\%\Delta EBIT}{\%\Delta Sales} = \frac{\text{Contribution margin}}{EBIT} \qquad DFL = \frac{\%\Delta EPS}{\%\Delta EBIT} = \frac{EBIT}{EBIT - \text{Interest}} \qquad DTL = DOL \times DFL
```

### G9 · Break-even

```math
Q_{BE} = \frac{\text{Fixed costs}}{P - VC} \qquad \text{Break-even revenue} = \frac{\text{Fixed costs}}{\text{Contribution margin ratio}} \qquad CM\ \text{ratio} = \frac{P - VC}{P}
```

P is the price per unit and VC the variable cost per unit.

### G10 · Altman Z-score (public manufacturers)

```math
Z = 1.2X_1 + 1.4X_2 + 3.3X_3 + 0.6X_4 + 1.0X_5
```

X₁ = working capital ÷ total assets; X₂ = retained earnings ÷ total assets; X₃ = EBIT ÷ total assets; X₄ = market value of equity ÷ total liabilities; X₅ = sales ÷ total assets. Above 2.99 is the safe zone, 1.81–2.99 the grey zone and below 1.81 the distress zone.

### G11 · Piotroski F-score (0 to 9)

Score 1 point for each test passed; 8–9 signals strength, 0–2 weakness.

| Area | Tests |
| --- | --- |
| Profitability | ROA positive; operating cash flow positive; ROA higher than last year; operating cash flow above net income |
| Leverage and liquidity | Long-term debt ratio lower than last year; current ratio higher; no new shares issued |
| Efficiency | Gross margin higher than last year; asset turnover higher |

### G12 · Beneish M-score (earnings manipulation screen)

```math
M = -4.84 + 0.920\,DSRI + 0.528\,GMI + 0.404\,AQI + 0.892\,SGI + 0.115\,DEPI - 0.172\,SGAI + 4.679\,TATA - 0.327\,LVGI
```

Each input is a year-on-year index: days' sales in receivables (DSRI), gross margin (GMI), asset quality (AQI), sales growth (SGI), depreciation (DEPI), SG&A (SGAI), total accruals to total assets (TATA) and leverage (LVGI). A score above about −1.78 flags a possible manipulator. Use it as a prompt for questions, not as proof.

### G13 · Industry metrics

| Industry | Metric | Formula |
| --- | --- | --- |
| Software | Rule of 40 | Revenue growth % + FCF margin %; 40 or more is healthy |
| Software | Net revenue retention | (Starting recurring revenue + expansion − contraction − churn) ÷ starting recurring revenue |
| Subscription | Customer lifetime value (LTV) | Revenue per customer × gross margin ÷ churn rate |
| Subscription | CAC payback (months) | Customer acquisition cost ÷ (monthly revenue per customer × gross margin) |
| Banks | Net interest margin | (Interest income − interest expense) ÷ average earning assets |
| Banks | Efficiency ratio | Non-interest expense ÷ revenue; lower is better |
| Banks | CET1 ratio | Common equity tier 1 capital ÷ risk-weighted assets |
| Insurance | Combined ratio | Loss ratio + expense ratio; below 100% is an underwriting profit |
| REITs | Funds from operations (FFO) | Net income + real-estate depreciation and amortization − gains on property sales |
| REITs | Adjusted FFO | FFO − recurring capex − straight-line rent adjustments |
| Real estate | Cap rate | Net operating income ÷ property value |
| Retail | Same-store sales growth | Sales growth at stores open at least a year |
| Airlines | Load factor | Revenue passenger miles ÷ available seat miles |
| Semiconductors | Book-to-bill | Orders received ÷ units shipped and billed; above 1 means demand is growing |

### G14 · Analytics shortcuts

```math
\text{YoY growth} = \frac{X_t}{X_{t-1}} - 1 \qquad \text{Common-size line} = \frac{\text{Line item}}{\text{Revenue (or total assets)}}
```

## H · Economics and macroeconomics

**H1 · GDP by expenditure**

```math
GDP = C + I + G + (X - M)
```

Consumption, investment, government spending and net exports.

**H2 · Real GDP and the GDP deflator**

```math
\text{Real GDP} = \frac{\text{Nominal GDP}}{\text{Deflator}/100} \qquad \text{Deflator} = \frac{\text{Nominal GDP}}{\text{Real GDP}} \times 100
```

**H3 · Growth accounting (Solow)**

```math
g_Y = g_A + \alpha\,g_K + (1 - \alpha)\,g_L
```

Output growth = productivity growth + capital share × capital growth + labor share × labor growth.

**H4 · Output gap**

```math
\text{Output gap} = \frac{\text{Actual GDP} - \text{Potential GDP}}{\text{Potential GDP}}
```

Positive means the economy is running hot (inflation pressure); negative means slack.

**H5 · Inflation and the CPI**

```math
\pi_t = \frac{CPI_t - CPI_{t-1}}{CPI_{t-1}} \qquad CPI = \frac{\text{Cost of basket today}}{\text{Cost of basket in base year}} \times 100
```

**H6 · Converting to real (today's) dollars**

```math
\text{Value in today's dollars} = \text{Past value} \times \frac{CPI_{\text{today}}}{CPI_{\text{then}}}
```

**H7 · Labor market**

```math
\text{Unemployment rate} = \frac{\text{Unemployed}}{\text{Labor force}} \qquad \text{Participation rate} = \frac{\text{Labor force}}{\text{Working-age population}}
```

**H8 · Sahm rule recession indicator**

```math
S_t = \overline{u}_{3m,t} - \min\left(\overline{u}_{3m}\text{ over the prior 12 months}\right)
```

A reading of 0.5 points or more has signaled the start of past US recessions.

**H9 · Okun's law (rule of thumb)**

```math
\Delta u \approx -0.5 \times (g_{\text{real GDP}} - g_{\text{potential}})
```

Growth 1 point below potential tends to raise unemployment by about half a point.

**H10 · Phillips curve (expectations-augmented)**

```math
\pi = \pi^{e} - \beta\,(u - u^{*}) + \text{supply shocks}
```

u\* is the natural rate of unemployment.

**H11 · Taylor rule**

```math
i = r^{*} + \pi + 0.5\,(\pi - \pi^{*}) + 0.5\,(y - y^{*})
```

r\* is the neutral real rate, π\* the 2% target and y − y\* the output gap in percent. It is a benchmark for where the policy rate "should" be, not what the Fed must do.

**H12 · Fisher equation and the real interest rate**

```math
(1 + i) = (1 + r)(1 + \pi^{e}) \qquad r \approx i - \pi^{e}
```

**H13 · Quantity theory of money**

```math
MV = PY \qquad \%\Delta M + \%\Delta V \approx \%\Delta P + \%\Delta Y
```

Money supply × velocity = price level × real output.

**H14 · Money multiplier (simple)**

```math
\text{Money multiplier} = \frac{1}{\text{Reserve ratio}}
```

A textbook upper bound; in practice banks' lending is constrained by capital and demand.

**H15 · Fiscal multipliers**

```math
k = \frac{1}{1 - MPC} = \frac{1}{MPS} \qquad k_{\text{tax}} = \frac{-MPC}{1 - MPC} \qquad k_{\text{open economy}} = \frac{1}{1 - MPC(1 - t) + MPM}
```

MPC + MPS = 1; t is the tax rate and MPM the marginal propensity to import. A balanced-budget change has a multiplier of 1.

**H16 · Government debt dynamics**

```math
\Delta d \approx (r - g)\,d - s
```

d is debt ÷ GDP, r the real interest rate on the debt, g real GDP growth and s the primary surplus ÷ GDP. When r exceeds g, the debt ratio rises unless the government runs a primary surplus.

**H17 · Elasticities**

```math
E_d = \frac{\%\Delta Q_d}{\%\Delta P} \qquad E_{\text{midpoint}} = \frac{(Q_2 - Q_1)/\left[(Q_1 + Q_2)/2\right]}{(P_2 - P_1)/\left[(P_1 + P_2)/2\right]}
```

Income elasticity = %ΔQ ÷ %Δincome; cross-price elasticity = %ΔQ of good x ÷ %ΔP of good y. When |E\_d| > 1 demand is elastic, and cutting price raises total revenue; when |E\_d| < 1 the firm has pricing power.

**H18 · Revenue, cost and profit**

```math
TR = P \times Q \qquad MR = \frac{\Delta TR}{\Delta Q} \qquad MC = \frac{\Delta TC}{\Delta Q} \qquad \text{Profit is maximized where } MR = MC
```

**H19 · Market concentration**

```math
HHI = \sum_{i} s_i^{2} \qquad CR_4 = s_1 + s_2 + s_3 + s_4
```

With market shares s in percent, HHI runs from near 0 (fragmented) to 10,000 (monopoly). Regulators treat markets in the high thousands as highly concentrated; check the current merger guidelines for thresholds.

**H20 · Exchange rates and parity conditions**

```math
\frac{F}{S} = \frac{1 + i_d}{1 + i_f} \qquad E(\%\Delta S) \approx i_d - i_f \qquad \%\Delta S \approx \pi_d - \pi_f
```

S and F are the spot and forward prices of one unit of foreign currency in domestic currency. The first is covered interest parity (a no-arbitrage condition), the second uncovered interest parity, and the third relative purchasing power parity; the last two hold only loosely and over long periods.

**H21 · Real exchange rate and home-currency return**

```math
\text{Real exchange rate} = S \times \frac{P_f}{P_d} \qquad R_{\text{home}} = (1 + R_{\text{local}})(1 + R_{FX}) - 1
```

**H22 · Trade and the balance of payments**

```math
\text{Terms of trade} = \frac{\text{Export price index}}{\text{Import price index}} \times 100 \qquad CA + KA + FA = 0
```

The current, capital and financial accounts sum to zero (net of errors and omissions).

**H23 · Rule of 70 (doubling time for any growth rate)**

```math
\text{Years to double} \approx \frac{70}{g \text{ in percent}}
```

At 2% real growth, an economy doubles in size in about 35 years.

## I · Personal finance, retirement and tax

**I1 · Household balance sheet and cash flow**

```math
\text{Net worth} = \text{Assets} - \text{Liabilities} \qquad \text{Savings rate} = \frac{\text{Annual savings}}{\text{Annual income}} \qquad DTI = \frac{\text{Monthly debt payments}}{\text{Gross monthly income}}
```

Lenders generally want a low debt-to-income ratio (DTI); many cap it somewhere around 36–45%.

**I2 · Emergency fund (rule of thumb)**

```math
\text{Emergency fund} = \text{Monthly essential expenses} \times (3 \text{ to } 6)
```

Use 6–12 months for irregular incomes and retirees.

**I3 · Cost of a goal in future dollars**

```math
\text{Future cost} = \text{Cost today} \times (1 + \pi)^{n}
```

**I4 · Savings needed to reach a goal**

```math
PMT = \left[FV_{\text{goal}} - PV(1 + r)^{n}\right] \times \frac{r}{(1 + r)^{n} - 1}
```

**I5 · Required return**

```math
FV_{\text{goal}} = PV(1 + r)^{n} + PMT\,\frac{(1 + r)^{n} - 1}{r} \quad \text{solve for } r
```

Use RATE in a spreadsheet, or Goal Seek when there are withdrawals along the way.

**I6 · Portfolio needed for retirement**

```math
\text{Annual gap} = \text{Spending} - \text{Social Security} - \text{Pensions} \qquad \text{Portfolio needed} \approx \frac{\text{Annual gap}}{\text{Withdrawal rate}}
```

At a 4% withdrawal rate, that is 25 times the annual gap. Planners often assume spending of 70–85% of pre-retirement income (the replacement ratio).

**I7 · Sustainable withdrawal (annuity method)**

```math
W = PV \times \frac{r}{1 - (1 + r)^{-n}} \qquad W_{\text{real}} \text{: use } r_{\text{real}} = \frac{1 + r}{1 + \pi} - 1
```

The level withdrawal that exhausts the portfolio in exactly n years. Using the real rate gives withdrawals that keep pace with inflation.

**I8 · Human capital (simplified)**

```math
HC_0 = \sum_{t=1}^{N}\frac{\text{Expected earnings}_t}{(1 + r_f + \text{risk premium})^{t}}
```

Add a larger risk premium for less stable careers.

**I9 · Life insurance need (income-replacement method)**

```math
\text{Need} \approx PV(\text{family's lost income and goals}) - \text{Existing assets and coverage}
```

**I10 · Tax rates**

```math
\text{Effective rate} = \frac{\text{Total tax}}{\text{Income}} \qquad \text{Marginal rate} = \text{tax on the next dollar}
```

Use the marginal rate for investment decisions.

**I11 · Capital gains tax**

```math
\text{Tax} = (P_{\text{sale}} - \text{Basis}) \times t_{cg} \qquad \text{After-tax proceeds} = P_{\text{sale}} - (P_{\text{sale}} - \text{Basis})\,t_{cg}
```

**I12 · Accrual vs deferred taxation**

```math
FV_{\text{taxed yearly}} = PV\left[1 + r(1 - t)\right]^{n} \qquad FV_{\text{taxed at sale}} = PV\left[(1 + r)^{n}(1 - t) + t\right]
```

The second formula taxes only the gain at the end (basis = PV). Deferral lets untaxed gains compound.

**I13 · Traditional vs Roth accounts**

```math
FV_{\text{traditional, after tax}} = C(1 + r)^{n}(1 - t_{\text{withdrawal}}) \qquad FV_{\text{Roth}} = C(1 - t_{\text{contribution}})(1 + r)^{n}
```

C is the pretax amount available to save. The two are equal when the tax rates today and at withdrawal are equal, so the choice turns on whether you expect your tax rate to rise or fall.

**I14 · Required minimum distribution**

```math
RMD = \frac{\text{Prior year-end account balance}}{\text{Distribution period (IRS Uniform Lifetime Table)}}
```

RMDs from traditional IRAs start at 73, rising to 75 for people born in 1960 or later.

**I15 · Social Security delayed retirement credits**

```math
\text{Benefit at claim age} \approx \text{Full benefit} \times (1 + 0.08 \times \text{years delayed past full retirement age})
```

Credits stop at age 70. With a full retirement age of 67, waiting until 70 raises the benefit by about 24%.

**I16 · US rules worth knowing**

| Rule | What it says |
| --- | --- |
| Long-term capital gains | Assets held more than a year: 0%, 15% or 20% federal rates depending on income |
| Net investment income tax | An extra 3.8% for higher earners |
| Short-term gains and interest | Taxed at ordinary income rates |
| Qualified dividends | Taxed at long-term capital-gains rates if the holding-period test is met |
| Collectibles, including physically backed gold ETFs | Long-term gains taxed at up to 28% |
| Capital losses | Offset gains, plus up to \$3,000 a year of ordinary income; the rest carries forward |
| Wash-sale rule | A loss is disallowed if a substantially identical security is bought within 30 days before or after the sale |
| Early withdrawals | Withdrawals from retirement accounts before 59½ generally incur a 10% penalty, with exceptions |
| Bank deposits | FDIC insurance covers up to \$250,000 per depositor, per insured bank, per ownership category |
| Brokerage accounts | SIPC protects up to \$500,000 per customer, including up to \$250,000 of cash, if a broker fails (not against market losses) |

Income thresholds change every year; check the IRS for the current figures.

**I17 · 2026 contribution limits**

| Account | 2026 limit |
| --- | --- |
| 401(k), 403(b), most 457 plans and the Thrift Savings Plan | \$24,500 |
| Catch-up, age 50 and over | \$8,000 |
| Catch-up, ages 60–63 | \$11,250 |
| Traditional or Roth IRA | \$7,500 |
| IRA catch-up, age 50 and over | \$1,100 |
| SIMPLE IRA | \$17,000, plus a \$4,000 catch-up |
| Roth IRA income phase-out, single filers | \$153,000–\$168,000 |
| Roth IRA income phase-out, married filing jointly | \$242,000–\$252,000 |

Source: [InvestmentNews, citing the IRS](https://www.investmentnews.com/retirement-planning/irs-reveals-new-401k-ira-contribution-limits-for-2026/263029).

## J · Options and derivatives essentials

S is the stock price, K the strike price, c and p the call and put premiums, T the time to expiry in years and r the risk-free rate.

**J1 · Payoffs at expiry**

```math
\text{Call} = \max(S_T - K,\,0) \qquad \text{Put} = \max(K - S_T,\,0)
```

The buyer's profit is the payoff minus the premium; the seller's profit is the premium minus the payoff.

**J2 · Intrinsic and time value**

```math
\text{Call intrinsic} = \max(S - K,\,0) \qquad \text{Put intrinsic} = \max(K - S,\,0) \qquad \text{Time value} = \text{Premium} - \text{Intrinsic value}
```

**J3 · Breakeven prices for option buyers**

```math
\text{Long call: } S_T = K + c \qquad \text{Long put: } S_T = K - p
```

**J4 · Put-call parity (European options)**

```math
c + K e^{-rT} = p + S_0
```

With known dividends, replace S₀ with S₀ minus the present value of the dividends.

**J5 · Protective put (own the stock, buy a put)**

```math
\text{Maximum loss} = S_0 - K + p \qquad \text{Breakeven} = S_0 + p
```

Insurance with unlimited upside, paid for by the premium.

**J6 · Covered call (own the stock, sell a call)**

```math
\text{Maximum gain} = K - S_0 + c \qquad \text{Maximum loss} = S_0 - c \qquad \text{Breakeven} = S_0 - c
```

Income now in exchange for capped upside.

**J7 · Collar (own the stock, buy a put at K₁, sell a call at K₂)**

```math
\text{Floor} = K_1 - S_0 - p + c \qquad \text{Cap} = K_2 - S_0 - p + c
```

Selling the call pays for some or all of the put. A "zero-cost collar" sets the strikes so that c = p.

**J8 · Black–Scholes–Merton**

```math
c = S_0 N(d_1) - K e^{-rT} N(d_2) \qquad p = K e^{-rT} N(-d_2) - S_0 N(-d_1)
```

```math
d_1 = \frac{\ln(S_0/K) + (r + \sigma^{2}/2)\,T}{\sigma\sqrt{T}} \qquad d_2 = d_1 - \sigma\sqrt{T}
```

For a stock with dividend yield q, replace S₀ with S₀e^(−qT) and r + σ²/2 with r − q + σ²/2.

**J9 · The Greeks**

| Greek | Measures | Value or sign for a long option |
| --- | --- | --- |
| Delta | Price change per \$1 move in the stock | Call N(d₁), between 0 and 1; put N(d₁) − 1, between −1 and 0 |
| Gamma | Change in delta per \$1 move | Positive; highest near the strike close to expiry |
| Theta | Value lost per day as time passes | Usually negative |
| Vega | Value change per 1-point change in implied volatility | Positive |
| Rho | Value change per 1-point change in interest rates | Positive for calls, negative for puts |

**J10 · Delta hedging**

```math
\text{Options needed to hedge} = \frac{\text{Shares held}}{\text{Delta per option}}
```

**J11 · Forward and futures pricing (cost of carry)**

```math
F_0 = S_0\,e^{(r - q)T} \qquad F_0 = S_0\,e^{(r + u - y)T}
```

The first is for an asset with income yield q; the second for a commodity with storage cost u and convenience yield y. Currency forwards follow covered interest parity (section H).

**J12 · Changing a portfolio's beta with index futures**

```math
N_f = \frac{(\beta_{\text{target}} - \beta_{\text{portfolio}}) \times V_p}{F \times \text{multiplier}}
```

A negative N\_f means selling contracts. A target beta of 0 fully hedges market risk.

**J13 · Minimum-variance hedge ratio**

```math
h^{*} = \rho\,\frac{\sigma_S}{\sigma_F} \qquad N^{*} = h^{*}\,\frac{Q_A}{Q_F}
```

σ\_S and σ\_F are the volatilities of the spot and futures price changes; Q\_A is the position size and Q\_F the size of one contract.

**J14 · Commodity futures return**

```math
R_{\text{futures index}} \approx \text{Spot return} + \text{Roll yield} + \text{Collateral return}
```

Roll yield is negative in contango (later contracts cost more) and positive in backwardation.

## K · Spreadsheet functions and rules of thumb

### K1 · Excel and Google Sheets functions

Rates and periods must match (a monthly rate with monthly periods). Money paid out is negative.

| Function | What it returns | Example |
| --- | --- | --- |
| FV(rate, nper, pmt, \[pv\], \[type\]) | Future value | =FV(5%, 10, 0, -100000) gives \$162,889 |
| PV(rate, nper, pmt, \[fv\], \[type\]) | Present value | =PV(8%, 5, 0, -1000) |
| PMT(rate, nper, pv, \[fv\], \[type\]) | Payment per period | =PMT(6%/12, 360, -400000) for a mortgage |
| NPER(rate, pmt, pv, \[fv\]) | Number of periods | Years to reach a goal |
| RATE(nper, pmt, pv, \[fv\]) | Rate per period | Required return for a goal |
| NPV(rate, values) | Present value of values starting one period from now | Add the time-0 cash flow separately |
| XNPV(rate, values, dates) | NPV with exact dates | DCF with irregular dates |
| IRR(values), XIRR(values, dates) | Internal rate of return | XIRR gives the money-weighted return |
| EFFECT(rate, npery), NOMINAL(rate, npery) | Effective or nominal annual rate | =EFFECT(6%, 12) gives 6.17% |
| AVERAGE, MEDIAN, GEOMEAN | Means | =GEOMEAN(1 + returns) − 1 for the geometric mean |
| STDEV.S, VAR.S | Sample standard deviation and variance | Monthly volatility × SQRT(12) to annualize |
| CORREL(x, y), COVARIANCE.S(x, y) | Correlation, covariance | Inputs for portfolio risk |
| SLOPE(y, x), INTERCEPT(y, x), RSQ(y, x) | Beta, alpha, R² of a regression | =SLOPE(stock returns, market returns) |
| LINEST(y, x-range, TRUE, TRUE) | Multiple regression with statistics | Factor regressions |
| SUMPRODUCT(weights, values) | Weighted sum | Portfolio expected return or duration |
| MMULT, TRANSPOSE | Matrix maths | Portfolio volatility (below) |
| NORM.S.INV(p), NORM.INV(p, mean, sd), NORM.DIST(x, mean, sd, TRUE) | Normal distribution | =NORM.S.INV(0.95) gives 1.645 |
| RAND() | Uniform random number | Monte Carlo draws (below) |
| PRICE, YIELD, DURATION, MDURATION | Bond price, YTM, Macaulay and modified duration | Need settlement and maturity dates |
| TBILLPRICE, TBILLYIELD, TBILLEQ | T-bill price, yield and bond-equivalent yield | Comparing bills with notes |
| ACCRINT | Accrued interest | Dirty price |
| XLOOKUP, INDEX with MATCH, SUMIFS | Lookups and conditional sums | Building comparison tables |
| GOOGLEFINANCE(ticker, attribute, start, end, interval) | Prices and history (Google Sheets only) | =GOOGLEFINANCE("VTI", "close", DATE(2021,1,1), TODAY(), "DAILY") |
| Data Table (What-If Analysis) | A grid of results for two changing inputs | DCF sensitivity to WACC and growth |
| Goal Seek | The input that hits a target | Implied growth in a reverse DCF |
| Solver add-in | Optimization with constraints | Minimum-variance weights |

**Portfolio volatility from weights w (a column) and covariance matrix Cov:**

```
=SQRT(MMULT(MMULT(TRANSPOSE(w), Cov), w))
```

**One Monte Carlo year of returns (copy across years and down 1,000+ rows):**

```
=NORM.INV(RAND(), expected_return, volatility)
```

**Linking a column of periodic returns into a cumulative return:**

```
=PRODUCT(1 + returns) - 1
```

Enter it as an array formula in older versions of Excel.

### K2 · Rules of thumb

| Rule | What it says | Caveat |
| --- | --- | --- |
| Rule of 72 | Years to double ≈ 72 ÷ rate; triple ≈ 114 ÷ rate; quadruple ≈ 144 ÷ rate | Approximate; least accurate at high rates |
| Duration rule | A 1-point rise in yields cuts a bond's price by about its duration in percent | Ignores convexity on large moves |
| Bond-fund horizon | Return ≈ starting yield over about 2 × duration − 1 years | Assumes a constant duration and no defaults |
| Loss recovery | −20% needs +25%, −33% needs +50%, −50% needs +100% | Exact: 1 ÷ (1 − loss) − 1 |
| 4% rule | Withdraw 4% of the starting portfolio, then raise it with inflation; historically lasted 30 years in the US | Not a guarantee; depends on returns, fees and horizon |
| 25× rule | Portfolio needed ≈ 25 × annual spending drawn from it | The inverse of the 4% rule |
| Emergency fund | 3–6 months of essential expenses | 6–12 months for irregular income or retirees |
| "110 minus age" | Rough share in stocks | Ignores the actual client; a starting point only |
| Diversification | 20–30 stocks across sectors remove most company-specific risk | Not market risk |
| Position limits | Common IPS limits: 5% per stock, 25% per sector | Set them from the client's risk profile |
| Fees | Over 30 years at 6% gross, a 1% fee takes about a quarter of the ending wealth | Exact: section D14 |
| Losing years | US stocks lost money in 26 of 96 calendar years from 1928 to 2023, about one in four | Losses cluster in recessions |
| Bear markets | The S&P 500 has entered a bear market about every 3.5 years on average since 1929 | Timing is unpredictable |
| Sharpe ratio | US stocks scored about 0.43 on annual data, 1928–2023 | Higher is better; compare like with like |
| Lump sum vs averaging in | Investing at once beat dollar-cost averaging about two-thirds of the time in Vanguard's research | Averaging in can still help a nervous client commit |
| Basis points | 100 basis points = 1 percentage point | "Up 25 bp" means up 0.25 points |
| Annualizing volatility | Monthly × √12; daily × √252 | Assumes independent returns |

## Sources

- [InvestmentNews: IRS reveals new 401(k), IRA contribution limits for 2026](https://www.investmentnews.com/retirement-planning/irs-reveals-new-401k-ira-contribution-limits-for-2026/263029): the 2026 limits in I17.
- [Damodaran Online: historical returns, 1928–2023](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histret.html): the US stock Sharpe ratio (D1) and losing-year count (K2), computed from its annual data.
- [Hartford Funds: S&P 500 bear markets](https://hartfordfunds.com/practice-management/client-conversations/managing-volatility/bear-markets.html): bear-market frequency (K2).

Formulas follow standard finance and economics texts and the CFA curriculum. Tax rules and thresholds change; confirm current figures with the IRS before relying on them.

---

[Key terms →](key-terms.md) · [Course contents](../course/README.md) · [Repo home](../README.md)
