# Installation Guide

This guide provides step-by-step instructions for setting up the necessary Conda environment and installing the transformation module.

## Setting Up the Conda Environment

Follow these steps to create and activate the required Conda environment:

### Step 1: Create the Conda Environment

Use the following command to create a Conda environment based on the `environment.yml` file. This file should list all the necessary dependencies.

```bash
conda env create -f environment.yml
```

### Step 2: Create the Conda Environment

Once the environment is successfully created, you can activate it using the following command:
```bash
conda activate garsh
```

# Installing the Transformation Module

To install the transformation module, follow these steps:

1. **Open your terminal or command prompt** and navigate to the directory containing the `setup.py` file of the transformation module.

2. **Run the following command**:

    ```bash
    pip install -e .
    ```

This command installs the transformation module in editable mode. This means that any changes you make to the source code will be immediately reflected in the module without needing to reinstall it.

## Usage

After installing the module, you can import it and use the classes or functions from the `transform` Python file in your projects as follows:

```python
from transformation import transform
# Your code using the module here
```


# TCS Stock Analysis

This repository contains the analysis and prediction of historical stock data for META up to November 2023. The project encompasses feature engineering, the development of a custom pipeline, and the application of various machine-learning models for stock price prediction.

## Feature Engineering

In this section, we focus on deriving new features from the raw stock data and selecting the most impactful ones for our models.

### 1. Calculating Technical Indicators
We calculate several technical indicators that are commonly used in stock market analysis:
- **RSI (Relative Strength Index)**
- **MACD (Moving Average Convergence Divergence)**
- **Bollinger Bands**
- **OBV (On-Balance Volume)**

### 2. Correlation Analysis
- We analyze the correlation between the various features.
- Based on this analysis, we reduce our feature set to those that are most influential.

### 3. Custom Pipeline
We create a custom pipeline for streamlined feature transformation:

```python
Pipeline(steps=[
    ('rsitransformer', RSITransformer()),
    ('macdtransformer', MACDTransformer()),
    ('bollingerbandstransformer', BollingerBandsTransformer()),
    ('obvtransformer', OBVTransformer()),
    ('nanremovaltransformer', NaNRemovalTransformer()),
    ('featureselector', FeatureSelector(selected_features=['RSI', 'MACD', 'OBV', 'High', 'Close']))
])
```

### 1.4 Creating a Python Module for the Pipeline
A Python module has been developed to facilitate the easy use of the feature transformation pipeline. This module streamlines the process of applying complex transformations like RSI, MACD, Bollinger Bands, and OBV to the stock data.

## Model Creation

### 2.1 Linear Model
- The initial implementation with a linear model did not perform well, even on the training data, indicating its unsuitability for this dataset.

### 2.2 Random Forest
- **Base Case Implementation**: A Random Forest model was implemented as a baseline.
- **Hyperparameter Tuning**: The model was further refined with hyperparameter tuning.
- **Scaling Techniques**: Different scaling techniques, including MinMax Scaler and StandardScaler, were tested.
- **Performance**: Despite improvements in MSE for both training and test data, the overall error remained high, leading to the exploration of other algorithms.

### 2.3 Support Vector Machine (SVM)
- **Base Case SVR**: Implemented a Support Vector Regressor (SVR) as a base model.
- **Hyperparameter Tuning**: Conducted extensive tuning of the SVR parameters, some of which were adjusted through a trial and error method.
- **Performance**: The optimized SVR model significantly outperformed the Random Forest model, reducing the MSE by 21 times.
- **Comparison**: The SVR with hyperparameter tuning proved to be much more effective than both the Random Forest Regressor and the Linear model.

### 2.4 Neural Network
- **Basic Neural Network**: Developed and implemented a basic Neural Network architecture.
- **Performance**: This model outperformed all the previous machine learning algorithms.
- **MSE Reduction**: Achieved an 8-fold reduction in Mean Squared Error (MSE) compared to the best-performing traditional machine learning model.

## Conclusion

This project highlights the effectiveness of various machine learning models in stock price prediction. The Neural Network and optimized Support Vector Regressor emerged as the most effective models, significantly reducing the prediction error compared to traditional machine learning approaches.

---

For more detailed information on the methodologies, code, and results, please refer to the Jupyter notebooks and Python scripts included in this repository.


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
