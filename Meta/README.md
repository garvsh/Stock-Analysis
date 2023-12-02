Using statistics and python to analyse stock prices.

1. META Stock Analysis:
    (Used all the historical data for META upto 2023-11)

    -> Meta_stock_visualization
    1. Plotting the closing price and volume over time to get a basic understanding of the stock's behavior
        To get an idea of daily stock close price and volume of stocks traded. This gives us the idea if the stock is moving upwards with time and also the fluctuations in stock. 
    
    2.  Stock's volatility
        We can calculate the daily returns, which are the percentage change in the closing price from one day to the next. This will give us an idea of how much the stock price fluctuates on a day-to-day basis
    
    3. Plot moving average
        The moving average smooths out price data to create a single flowing line, making it easier to identify the direction of the trend
    
    4. Time series visualization
        4.1 Trend: This shows the long-term movement in the data, smoothing out short-term fluctuations.
    
        4.2 Seasonality: This represents regular patterns or cycles in the data. In this case, we used a 365-day period to look for yearly patterns.
    
        4.3. Residual: These are the irregularities or 'noise' left after removing the trend and seasonality. This component can sometimes reveal anomalies or non-recurring events.

    5. Anamoly detection
        Anomalies are identified using a standard Z-score threshold (>3), which flags data points that deviate significantly from the average.
    
    6. Price and Moving Average Crossover
        Crossovers:
        6.1. Bullish Crossover: Marked with green triangles (^), occurs when the MA20 crosses above the MA50. This is often interpreted as a buy signal, suggesting that the stock might be entering an uptrend.
        6.2. Bearish Crossover: Marked with red triangles (v), occurs when the MA20 crosses below the MA50. This is often seen as a sell signal, indicating that the stock might be heading into a downtrend.


    -> Meta Algorithmic Trading Strategy:
    1.  Basic strategy by using rolling mean

        Observations: 
        1. Our strategy is underperforming as compared to daily returns, but the risk is less as it does not go down as the stock price go down
        2. At the final stages when the market is more volatile, our strategy is stable.
    
    2. Momentum Strategy

        Steps Used:
        1. Calculate the Rate of Change (ROC):
        The ROC can be calculated as the percentage change in the closing price over a certain number of days (e.g., 14 days).
        2. Generate Trading Signals:
            2.1 Buy Signal: When the ROC is positive and exceeds a certain threshold, indicating upward momentum.
            2.2 Sell Signal: When the ROC is negative or falls below a certain threshold, indicating downward momentum.
        3. Backtest the Strategy: Apply these signals to historical data to simulate trades and calculate returns.
        4. Evaluate Performance: Assess the strategy's performance by comparing the returns of the strategy to the market.
    
        <h3>Observations </h3>
        1. Our strategy is clearly underperforming.
        2. Momentum strategy is even worse than rolling mean strategy.

    3. Similarly tried Weighted Moving Average Strategy and the result was not good

    4. Machine Learning Algorithm:
        4.1. Performed EDA for feature creation(Rolling mean, ROI etc), feature selection and creating final training dataset
        4.2 Trained on a basic Logistic Regression model
        4.3 Hyper parameter Tuning
        4.4. Final Observation: Our strategy is doing well initally but on the later stage when there is a boom in the stock price, it is not picking up.

