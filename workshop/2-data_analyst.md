### 💡 Real-World Practice Data

This is a hands-on exercise with **real NASDAQ-100 stock market data** covering 5 years (2020-2025). You'll practice analyzing actual financial data and creating investment recommendations - skills directly applicable to finance, investing, and data science careers.

To use the real data for practice, run: `python3 download_nasdaq100.py`


## Stock Market Data Analysis

### Persona and Context Setting
```text
You are a Senior Stock Market Analyst with 10 years of experience in equity research, financial modeling, and market trend analysis. You specialize in identifying investment opportunities, patterns, and actionable insights from complex financial data. Communication style: Professional, data-driven, and focused on financial impact. I am uploading NASDAQ-100 dataset for 5 years (Oct 2020 – Oct 2025). Respond to my following queries in the format I specify.
```

### Data Assessment

**Prompt:**
```text
Assess the dataset quality: 
- Check data completeness and accuracy 
- Identify missing values, outliers, or inconsistencies 
- Verify date range and data frequency 
- Give it in a format with simple and precise summary and in a tabular form 
```

### Descriptive Analysis

**Prompt:**
```text
Perform a descriptive analysis:
- Perform a descriptive analysis:
- Summarize key statistics (mean, std dev, min, max)
- Calculate returns, volatility, and overall growth
- Identify trends in price and volume
- Give it in a format with simple summary and in a tabular form
```

### Comparative Analysis

**Prompt:**
```text
Compare performance over time:
- Identify trend shifts, highs/lows, and major corrections
- Compare periods (2021 vs 2023, etc.)
- Also provide some graphical representations
- Use table format and a small summary
```

### Insight Generation

**Prompt:**
```text
Generate insights:
- What patterns stand out?
- Why do they exist (macroeconomic or sector drivers)?
- What are the key takeaways for investors?
- Give a small paragraph with these insights
```

### Recommendations

**Prompt:**
```text
Provide actionable investment recommendations:
- Summarize short, medium, and long-term views
- Suggest entry, exit, and target zones
- Include risk factors and rationale
- Provide it in a Tablular and bullet points format
```

### Extras - NASDAQ-100 vs Bank FD Comparison

**Prompt:**
```text
Compare NASDAQ-100 performance against US bank FD returns over the same 5-year period.
Highlight key trade-offs in return, risk, liquidity, and inflation-adjusted growth.
```