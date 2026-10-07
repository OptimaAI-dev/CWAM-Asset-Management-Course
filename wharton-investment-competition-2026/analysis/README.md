# Analysis scripts

Two short Python scripts that reproduce the numbers in the course, so you can check them and rerun them with your own client's figures.

| Script | What it does | Where the numbers appear |
|---|---|---|
| [`worked_example.py`](worked_example.py) | Required return, expected return and volatility, value at risk, stress tests in dollars, risk contributions, Monte Carlo probability of reaching the goal, and what-if comparisons | [Appendix · Worked example](../course/17-appendix-worked-example.md) |
| [`history.py`](history.py) | Long-run US returns for stocks, bonds, bills and gold; every stock/bond mix from 0% to 100% stocks; stock-bond correlations by period | [Module 1](../course/01-investment-foundations.md), [Module 9](../course/09-alternatives-and-real-assets.md), [Module 10](../course/10-know-your-client.md), [Module 14](../course/14-risk-assessment-and-management.md) |

## Run them

You need Python 3.9 or later.

```bash
cd analysis
pip install -r requirements.txt
python worked_example.py
python history.py
```

## Use it for the Laura Gao case

Open `worked_example.py` and edit only the `INPUTS` block at the top:

1. **Client:** starting assets, yearly savings, withdrawals by year, the goal and the number of years.
2. **Risk limit:** `LOSS_LIMIT`, the largest calendar-year loss allowed by the IPS.
3. **Portfolio:** each sleeve's weight (weights must add up to 100%).
4. **Assumptions:** expected returns, volatilities and correlations. The ones in the file are illustrative teaching numbers. Replace them with a published set of capital market assumptions (Vanguard, BlackRock or J.P. Morgan publish theirs) and cite it in the report.
5. **Scenarios:** stress-test returns for each sleeve, in percent.

Then run it again and read the stress-test and what-if lines against the IPS.

## Data

`data/damodaran_annual_returns_1928_2023.csv` holds annual returns in percent for the S&P 500 (dividends reinvested), 3-month T-bills, 10-year Treasury bonds, Baa corporate bonds, US home prices and gold. Source: Aswath Damodaran, NYU Stern, [Historical Returns on Stocks, Bonds and Bills](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histret.html), the update covering 1928–2023. Gold figures are only meaningful from 1971, when gold began trading freely.
