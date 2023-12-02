# META Stock Analysis

Analysis of all historical data for META up to November 2023.

## Meta_stock_visualization

### 1. Plotting the Closing Price and Volume Over Time

- **Objective**: To understand the stock's behavior by observing the daily stock close price and volume of stocks traded.

### 2. Stock's Volatility

- **Method**: Calculate the daily returns as the percentage change in the closing price from one day to the next.

### 3. Plot Moving Average

- **Purpose**: To identify the direction of the trend by smoothing out price data.

### 4. Time Series Visualization

- **4.1 Trend**: Shows long-term movement, smoothing out short-term fluctuations.
- **4.2 Seasonality**: Identifies regular patterns or cycles over a 365-day period.
- **4.3 Residual**: Examines irregularities or 'noise' after removing trend and seasonality.

### 5. Anomaly Detection

- **Method**: Using a standard Z-score threshold (>3) to flag significant deviations.

### 6. Price and Moving Average Crossover

- **6.1 Bullish Crossover**: Marked with green triangles (^), occurs when MA20 crosses above MA50.
- **6.2 Bearish Crossover**: Marked with red triangles (v), occurs when MA20 crosses below MA50.

## Meta Algorithmic Trading Strategy

### 1. Basic Strategy Using Rolling Mean

- **Observations**:
  1. Underperforms compared to daily returns but with less risk.
  2. Stable during volatile market phases.

### 2. Momentum Strategy

- **Steps**:
  1. Calculate the Rate of Change (ROC).
  2. Generate Trading Signals (Buy when ROC is positive and exceeds a threshold; Sell when ROC is negative or below a threshold).
  3. Backtest the Strategy.
  4. Evaluate Performance.

- **Observations**:
  1. Strategy underperforms.
  2. Worse performance than rolling mean strategy.

### 3. Weighted Moving Average Strategy

- **Result**: Not effective.

### 4. Machine Learning Algorithm

- **4.1. EDA**: Feature creation (Rolling mean, ROI, etc.), feature selection, and training dataset preparation.
- **4.2. Model Training**: Basic Logistic Regression model.
- **4.3. Hyperparameter Tuning**.
- **4.4. Final Observation**: Performs well initially but fails to capitalize on later stock price booms.
