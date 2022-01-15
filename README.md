# Intuitive Trading App

Our intuitive algorithmic trading application is a concept of allowing a user to be more in tune with purchasing and selling stocks, currency, fixed income instruments, and crypto currency. With newer and easier applications to allow a new and more diverse group of traders, there are limited applications which intuitively notify the user based on their trading patterns.  Machine learning is used in this application to study previous trading pattern behavior, and we use the predictions of the algorithm to notify the user of trades and positions taken as the machine learning algorithms predict them.

Our Machine Learning trading bot uses SVC and Logistic Regression Machine Learning to determine if a buy or sell should be done. Our only additional condition for a sell trade is if we currently have a long position. In other words, we only sell to close out a buy position, and never do a sell trade in order to go short the market.

We use SMAs and Bollinger Bands technical analysis indicators to feed the machine learning algorithms. Additionally, we have a function that cycles through various short and long windows for the moving average indicators to determine which combination of windows are the best. Within the same function, we also loop through various training period time frames to determine what is the best way to split our data into training and testing datasets for the algorithms.

After the machine learning algorithms are complete we also keep track of our position, and our portfolio holdings as we cycle through all the dates of the dataset.

We also decided to leverage Amazon's AWS Lex chat bot to create a more personalized experience for the client using our application. Through the chat bot, the client can be given recommendations of what other instruments they might be interested in investing in. For example, if a client picks a more high volatility stock like Tesla, our bot recommends other high volatility instruments such as Gamestop or Bitcoin.  If the client agrees, this instrument can easily be worked into the portfolio and be a part of the algorithm trading bot.

We will quickly define what is accuracy, precision, and recall as we think it would be helpful.

Accuracy = (number of True Positives + number of True Negatives) / Number of all datapoints (True and False Positives and Negatives)

Precision = (number of true positives) / (number of true positives + number of false positives)
So this number answers of all the positives you got, how many were correctly identified as positives?

Recall = (number of true positives) / (number of true positives + number of false negatives)
This metric asks of all the real world positives that were in the dataset, how many of them did the model identify?

---

## Technologies

The team is using python version 3.7.10 and is importing the following from the built-in libraries and from functions created within the team:

# Imports
import pandas as pd
import numpy as np
from pathlib import Path
import hvplot.pandas
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from pandas.tseries.offsets import DateOffset
from sklearn.metrics import classification_report
from finta import TA
%matplotlib inline

---

## Installation Guide

The Portfolio Analysis Application leverages Python version 3.7.10 and Git version 2.33.0.windows.2.

---

## Usage

To use the application, launch jupyter lab from the gitbash terminal and run the 'TradingBot_OptimizedSMAs.ipynb' noteback from the webpage. The client is free to change what instrument he wants to use by specifying which csv file to use for the application to feed the machine learning algorithms.  After that has been specified, the code could be run.

---

## Contributors

The contributors are Paul Lopez, Chaim Kriger, Isaac Iskra, Horayra Hossain

---

## License
No licenses required. Just get the consent of the contributors above and everything should be fine.
Chaim would like a tip :)
