# Financial Data Analysis Tool

> A Python-based financial analysis pipeline that ingests daily revenue and expense data, computes profitability metrics, and delivers actionable visual insights for business decision-making.

---

## Overview

This project demonstrates an end-to-end financial data workflow — from raw data ingestion to automated analysis and visualization. Built with Python and pandas, it is designed to give finance and operations teams a fast, reproducible way to monitor business performance over time.

**Tech Stack:** Python 3.14 · pandas 3.0 · matplotlib 3.10 · openpyxl · NumPy

---

## Key Findings

Analysis of a 30-day operating period (January 2026) revealed the following:

| Metric | Value |
|---|---|
| Total Revenue | $807,077 |
| Total Expenses | $539,679 |
| **Total Profit** | **$267,398** |
| Profit Margin | 33.1% |
| Avg. Daily Revenue | $26,902 |
| Avg. Daily Profit | $8,913 |
| Profitable Days | 22 of 30 |
| Loss Days | 8 of 30 |
| Best Day | Jan 3 (+$39,602) |
| Worst Day | Jan 29 (−$17,672) |

**Summary:** The business operated at a healthy 33% profit margin over the period, with profitability achieved on 73% of trading days. The 8 loss days were concentrated around mid-month and late January, suggesting potential exposure to cyclical expense spikes worth investigating further.

---

## Financial Overview Chart

![30-Day Financial Overview](data/financial_chart.png)

The chart plots daily Revenue and Expenses as trend lines, with profit/loss shading to immediately surface periods of financial stress vs. strong performance.

---

## Business Value

This analysis pipeline delivers value across three dimensions:

**1. Real-Time Performance Monitoring**
Finance teams can replace manual spreadsheet reviews with an automated script that produces up-to-date metrics and charts on demand — reducing reporting time from hours to seconds.

**2. Early Warning on Loss Days**
By flagging days where expenses exceed revenue (red shading), operations teams can investigate root causes proactively rather than discovering shortfalls at month-end.

**3. Scalability**
The pipeline is designed to scale from 30-day snapshots to multi-year datasets with no code changes — simply update the data in `/data` and re-run `analyze.py`.

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/ArturoPerez510/financial-analysis-project.git
cd financial-analysis-project
```

**2. Set up the environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy matplotlib openpyxl
```

**3. Generate data and run analysis**
```bash
python data/generate_data.py
python analyze.py
```

---

## Project Structure

```
financial-analysis-project/
├── analyze.py              # Main analysis and visualization script
├── data/
│   ├── generate_data.py    # Dummy data generator
│   ├── financial_data.csv  # 30-day financial dataset
│   └── financial_chart.png # Generated chart output
└── CLAUDE.md               # Project configuration notes
```

---

## Author

**Arturo Perez** · [GitHub](https://github.com/ArturoPerez510)
