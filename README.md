# Financial Analysis Project

A financial data analysis tool built with Python and pandas that generates and analyzes 30 days of financial data.

## Features

- Generates dummy financial data (Date, Revenue, Expenses, Profit)
- Analyzes data using pandas
- Visualizes results with matplotlib

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy matplotlib openpyxl
```

## Usage

Generate the data:
```bash
python data/generate_data.py
```

Run the analysis:
```bash
python analyze.py
```

## Output

![30-Day Financial Overview](data/financial_chart.png)
