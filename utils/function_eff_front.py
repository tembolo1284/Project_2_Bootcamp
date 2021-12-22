import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sn

def efficient_frontier(assets):
    pf_data = pd.DataFrame()
    for x in assets:
        pf_data[x] = wb.DataReader(x, data_source = 'yahoo', start = '2016-1-1')['Adj Close']

    # Graph of adjusted close of stocks
    (pf_data / pf_data.iloc[0]*100).plot(figsize=(10,5))

    # log returns of stocks
    log_returns = np.log(pf_data/pf_data.shift(1))
    log_returns.mean() * 252

    # covariance results
    log_returns.cov() * 252

    # correlation results
    log_returns.corr()

    # Heatmap - covariance matrix
    corrMat = log_returns.corr()
    sn.heatmap(corrMat, annot=True)
    plt.show()

    # calculating portfolio returns and volatility
    portfolio_returns = []
    portfolio_volatilities = []
    for x in range(1000):
        weights = np.random.random(len(assets))
        weights /= np.sum(weights)
    
        portfolio_returns.append(np.sum(weights * log_returns.mean()) * 252)
        portfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 252, weights))))
                    
    portfolio_returns = np.array(portfolio_returns)
    portfolio_volatilities = np.array(portfolio_volatilities)
                                  
    portfolio_returns, portfolio_volatilities

    np.sum(weights * log_returns.mean()) * 252
    np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 252, weights)))

    # Graph of efficient frontier
    portfolios = pd.DataFrame({'Return': portfolio_returns, 'Volatility':portfolio_volatilities  })
    portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(20,15))
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')

    pf_data
    ret_data = pf_data.pct_change()[1:]
    ret_data

    weighted_returns = (weights * ret_data)
    print(weighted_returns.head())

    port_ret = weighted_returns.sum(axis=1)
    port_ret

    cumulative_ret = (port_ret + 1).cumprod()
    cumulative_ret
    
    fig = plt.figure()
    ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
    ax1.plot(cumulative_ret)
    ax1.set_xlabel('Date')
    ax1.set_ylabel("Cumulative Returns")
    ax1.set_title("Portfolio Cumulative Returns")
    plt.show();
    ((pf_data+1).cumsum()).plot()
    
     # allocation of weights to each asset - calculation
    return weights


if __name__ == "__main__":

    efficient_frontier(['FB', 'AAPL', 'TSLA', 'RDS.A', 'GS'])



