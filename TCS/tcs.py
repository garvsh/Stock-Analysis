# Import necessary libraries
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import make_pipeline
import pandas as pd

# Define your custom transformers

from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

# RSI Transformer
class RSITransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()
        X_transformed['RSI'] = calculate_rsi(X_transformed['Close'])
        return X_transformed

# MACD Transformer
class MACDTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()
        macd, signal, hist = calculate_macd(X_transformed['Close'])
        X_transformed['MACD'] = macd
        X_transformed['MACDsignal'] = signal
        X_transformed['MACDhist'] = hist
        return X_transformed

# Bollinger Bands Transformer
class BollingerBandsTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()
        upper_band, middle_band, lower_band = calculate_bollinger_bands(X_transformed['Close'])
        X_transformed['BB_upper'] = upper_band
        X_transformed['BB_middle'] = middle_band
        X_transformed['BB_lower'] = lower_band
        return X_transformed

# OBV Transformer
class OBVTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()
        X_transformed['OBV'] = calculate_obv(X_transformed['Close'], X_transformed['Volume'])
        return X_transformed
    
class NaNRemovalTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X.dropna()

# Moving Average Transformer
class MovingAverageTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, column='Close', window=20):
        self.column = column
        self.window = window

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()
        X_transformed[f'SMA_{self.window}'] = X_transformed[self.column].rolling(window=self.window).mean()
        return X_transformed

class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, selected_features):
        self.selected_features = selected_features

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X[self.selected_features]

# Calculating RSI, MACD, Bollinger Bands, and OBV

# RSI (Relative Strength Index)
def calculate_rsi(data, window=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# train_data['RSI'] = calculate_rsi(train_data['Close'])

# MACD (Moving Average Convergence Divergence)
def calculate_macd(data, fastperiod=12, slowperiod=26, signalperiod=9):
    fast_ema = data.ewm(span=fastperiod, adjust=False).mean()
    slow_ema = data.ewm(span=slowperiod, adjust=False).mean()
    macd = fast_ema - slow_ema
    signal_line = macd.ewm(span=signalperiod, adjust=False).mean()
    macd_histogram = macd - signal_line
    return macd, signal_line, macd_histogram

# train_data['MACD'], train_data['MACDsignal'], train_data['MACDhist'] = calculate_macd(train_data['Close'])

# Bollinger Bands
def calculate_bollinger_bands(data, window=20, num_std=2):
    sma = data.rolling(window=window).mean()
    rstd = data.rolling(window=window).std()
    upper_band = sma + num_std * rstd
    lower_band = sma - num_std * rstd
    return upper_band, sma, lower_band

# train_data['BB_upper'], train_data['BB_middle'], train_data['BB_lower'] = calculate_bollinger_bands(train_data['Close'])

# On-Balance Volume (OBV)
def calculate_obv(close_prices, volumes):
    obv = [0]
    for i in range(1, len(close_prices)):
        if close_prices.iloc[i] > close_prices.iloc[i-1]:
            obv.append(obv[-1] + volumes.iloc[i])
        elif close_prices.iloc[i] < close_prices.iloc[i-1]:
            obv.append(obv[-1] - volumes.iloc[i])
        else:
            obv.append(obv[-1])
    return pd.Series(obv, index=close_prices.index)

# train_data['OBV'] = calculate_obv(train_data['Close'], train_data['Volume'])


# Function to apply the transformation pipeline
def transform_stock_data(df):
    # Selected features for the model
    selected_features = ['RSI', 'MACD', 'OBV', 'SMA_20', 'Close']


    # Creating the pipeline
    pipeline = make_pipeline(
        RSITransformer(),
        MACDTransformer(),
        BollingerBandsTransformer(),
        OBVTransformer(),
        MovingAverageTransformer(),
        NaNRemovalTransformer(),
        FeatureSelector(selected_features)
    )

    return pipeline.fit_transform(df)

# You can now import this module in a Jupyter Notebook and use the transform_stock_data function
# to transform any stock data DataFrame.
