# Wharton Investment Competition 2026–27 · Team study guide

Everything the team needs to analyze the Laura Gao case and build her portfolio: a 16-module course on investing, business analysis and portfolio management, a formula and key-terms booklet, fill-in templates, and scripts that reproduce the course's numbers.

> [!IMPORTANT]
> **The competition's rule on AI.** These materials were drafted with an AI assistant (Claude). Wharton allows generative AI for brainstorming and idea generation, but AI-generated work may not be submitted as your own, and any AI-generated material you use must be cited ([Rules & Roles](https://globalyouth.wharton.upenn.edu/?p=16670)). Use this repo to learn, then write every deliverable in your own words.

## What's inside

| Folder | What it holds |
|---|---|
| [`course/`](course/README.md) | The course, one file per module, plus a worked example from client file to finished portfolio |
| [`booklet/`](booklet/README.md) | The [formula booklet](booklet/formulas.md) (sections A–K) and the [key terms](booklet/key-terms.md) (acronyms A–Z and jargon by theme) |
| [`templates/`](templates/README.md) | Fill-in IPS, client profile, investment thesis, company tear sheet and trade log |
| [`analysis/`](analysis/README.md) | Python scripts that reproduce the worked example and the historical tables, ready for Laura's numbers |
| [`pdf/`](pdf/) | Print-ready PDFs of the course and the booklet |
| [`images/`](images/) | The course's charts and diagrams |

## Key dates (5:00 p.m. ET)

| Deliverable | Due |
|---|---|
| Official team roster | October 9, 2026 |
| Trading Notes Analysis | October 23, 2026 |
| Investment Policy Statement | November 6, 2026 |
| Final report and school documentation | December 4, 2026 |

Source: [Wharton Global Youth, 2026–27 competition page](https://globalyouth.wharton.upenn.edu/competitions/investment-competition/). The instructions Wharton sent registered teams set the formats and length limits.

## Where to start

Everyone reads [Start here](course/00-start-here.md), then the critical path: Modules [10](course/10-know-your-client.md), [11](course/11-investment-policy-statement.md), [12](course/12-portfolio-theory-and-asset-allocation.md), [14](course/14-risk-assessment-and-management.md) and [16](course/16-competition-playbook.md). After that, split by role:

| Role | Modules to own |
|---|---|
| Team leader and portfolio manager | [10](course/10-know-your-client.md), [11](course/11-investment-policy-statement.md), [12](course/12-portfolio-theory-and-asset-allocation.md), [16](course/16-competition-playbook.md) |
| Client and IPS lead | [10](course/10-know-your-client.md), [11](course/11-investment-policy-statement.md) |
| Macro and allocation analyst | [2](course/02-economics-for-investors.md), [12](course/12-portfolio-theory-and-asset-allocation.md) |
| Equity analysts | [3](course/03-business-management-and-strategy.md), [4](course/04-financial-statements-and-business-analytics.md), [5](course/05-analyzing-company-growth.md), [6](course/06-equity-valuation.md), [13](course/13-portfolio-construction-and-implementation.md) |
| Fixed income and ETF analyst | [7](course/07-fixed-income-and-tips.md), [8](course/08-etfs-funds-and-index-investing.md), [9](course/09-alternatives-and-real-assets.md) |
| Risk and performance analyst | [14](course/14-risk-assessment-and-management.md), [15](course/15-performance-measurement-and-reporting.md) |

The next deliverable after the trading notes is the IPS: start from [`templates/ips-template.md`](templates/ips-template.md) and [Module 11](course/11-investment-policy-statement.md).

## Accuracy notes

- Every worked calculation was re-run in code, and the [analysis scripts](analysis/README.md) reproduce them.
- Figures labelled "approximate" are rounded long-run historical numbers. Verify them before citing.
- Tickers are examples to research, never recommendations.
- The worked example uses a fictional client. Apply the same steps to the Laura Gao file.
- The pages behind the data are listed in [`course/sources.md`](course/sources.md).

## Live versions

The course and booklet started as Claude Docs, which take inline comments: [course](https://claude.ai/code/artifact/28eb6582-3e95-41d5-bcf7-7599a682ef05) · [booklet](https://claude.ai/code/artifact/f2009ca3-21ec-432c-b165-4f955364ae71). They stay private unless Carlos shares them, so this repo is the team's copy. Suggest fixes by opening an issue or a pull request.
