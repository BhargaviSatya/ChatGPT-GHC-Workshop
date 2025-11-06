# Prerequisites

# 1. Python 3.9+ must be installed.
#    - Windows: Download from https://www.python.org and check "Add Python to PATH"
#    - Linux (Ubuntu/Debian): sudo apt install python3 python3-venv python3-pip -y
#    - Mac: brew install python
#
# 2. Create and activate a virtual environment (recommended):
#    - Windows (PowerShell):
#        python -m venv venv
#        .\venv\Scripts\activate
#    - Linux / Mac:
#        python3 -m venv venv
#        source venv/bin/activate
#
# 3. Upgrade pip (inside the virtual environment):
#        pip install --upgrade pip
#
# 4. Install required Python packages:
#        pip install yfinance pandas numpy pytz
#    - yfinance: download historical OHLCV, dividends, splits from Yahoo Finance
#    - pandas: data manipulation and CSV export
#    - numpy: dependency for pandas
#    - pytz: ensures proper timezone handling
#
# 5. Verify installation:
#        python -c "import yfinance; import pandas; import numpy; import pytz; print('All packages installed!')"


import yfinance as yf
import pandas as pd

def main():
    # NASDAQ-100 index ticker
    ticker = "^NDX"
    
    start_date = "2020-10-01"
    end_date = "2025-11-04"

    print(f"Downloading {ticker} data from {start_date} to {end_date}...")

    # Download OHLCV
    data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False, progress=True)

    # Flatten MultiIndex columns if any
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]

    # Download dividends and stock splits (usually 0 for index)
    ticker_obj = yf.Ticker(ticker)
    dividends = ticker_obj.dividends[start_date:end_date].rename("Dividends").to_frame()
    splits = ticker_obj.splits[start_date:end_date].rename("Stock Splits").to_frame()

    # Make dividends and splits timezone-naive
    dividends.index = dividends.index.tz_localize(None)
    splits.index = splits.index.tz_localize(None)

    # Merge OHLCV with dividends and splits
    data = data.merge(dividends, left_index=True, right_index=True, how="left")
    data = data.merge(splits, left_index=True, right_index=True, how="left")

    # Fill missing values
    data["Dividends"].fillna(0, inplace=True)
    data["Stock Splits"].fillna(0, inplace=True)

    # Reset index to get Date column
    data.reset_index(inplace=True)

    # Ensure Date column has time component
    data["Date"] = data["Date"].dt.strftime("%Y-%m-%d %H:%M:%S")

    # Reorder columns
    columns_order = ["Date", "Open", "High", "Low", "Close", "Volume", "Dividends", "Stock Splits"]
    data = data[columns_order]

    # Save to CSV
    output_file = "nasdaq100_index_data.csv"
    data.to_csv(output_file, index=False)

    print(f"✅ Download complete! Data saved to '{output_file}'")

if __name__ == "__main__":
    main()
