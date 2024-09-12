# Technical Analysis utility using TA-Lib

import yfinance as yf
import talib as ta
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

pio.renderers.default = 'browser'

ticker = 'T'
start_date = '2024-01-01'
end_date = '2024-09-10'

df = yf.download(ticker, start_date, end_date)

# Simple moving average over 20 days
df['SMA'] = ta.SMA(df['Close'], timeperiod=20)

# Relative Strength Indicator over 14 days
df['SMA'] = ta.RSI(df['Close'], timeperiod=14)

# Upper, Lower and Middle Bollinger Band
df['Upper_BB'], df['Middle_BB'], df['Lower_BB'] = ta.BBANDS(df['Close'], timeperiod=20, nbdevup=1, nbdevdn=2, matype=0)

fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                    vertical_spacing=0.2, row_heights=[0.7, 0.3],
                    subplot_titles=[f'{ticker} Price and Indicators', 'RSI'])

candlestick = go.Candlestick(
    x=df.index,
    open=df.Open,
    high=df.High,
    low=df.Low,
    close=df.Close,
    name='Price'
)
sma_line = go.Scatter(
    x=df.index,
    y=df.SMA,
    line={'color': 'blue', 'width' : 2}
)
fig.add_trace(candlestick, row=1, col=1)

fig.update_layout(
    title=f'{ticker} Technical Analysis',
    yaxis_title='Price',
    xaxis_title='Date',
    xaxis_rangeslider_visible=False,
    height=800,
    template='plotly_dark'
)

fig.show()