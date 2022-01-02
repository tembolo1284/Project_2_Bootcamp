# Machine Learning Trading Bot Application

Our Machine Learning trading bot using SVC and Logistic Regression Machine Learning algorithms to determine if a buy or sell should be done. Our only additional condition for a sell trade is if we currently have a long position. In other words, we only sell to close out a buy position, and never do a sell trade in order to go short the market.

We use SMAs and MACD technical analysis indicators to feed the machine learning algorithms. Additionally, we have a function that cycles through various short and long windows for the moving average indicators to determine which combination of windows are the best. Within the same function, we also loop through various training period time frames to determine what is the best way to split our data into training and testing datasets for the algorithms.

After the machine learning algorithms are complete we also keep track of our position, and our portfolio holdings as we cycle through all the dates of the dataset.


We will quickly define what is accuracy, precision, and recall as we think it would be helpful.

Accuracy = (number of True Positives + number of True Negatives) / Number of all datapoints (True and False Positives and Negatives)

Precision = (number of true positives) / (number of true positives + number of false positives)
So this number answers of all the positives you got, how many were correctly identified as positives?

Recall = (number of true positives) / (number of true positives + number of false negatives)
This metric asks of all the real world positives that were in the dataset, how many of them did the model identify?

---

## Technologies

The team is using python version 3.7.10 and is importing the following from the built-in libraries and from functions created within the team:

import questionary
import os
import requests
import json
import sys
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from pandas_datareader import data as wb
from MCForecastTools import MCSimulation
%matplotlib inline

---

## Installation Guide

The Portfolio Analysis Application leverages Python version 3.7.10 and Git version 2.33.0.windows.2.

---

## Usage

To use the application, launch jupyter lab from the gitbash terminal and run the 'portfolio_analysis.ipynb' noteback from the webpage. Ensure the 'MCForecastTools.py' file, 'gitignore' file, and '.env' files are in the dir]\ectory where you run 'portfolio_analysis.ipynb'.
The user will be asked to input a portfolio amount, and their risk tolerence. The user will be asked to choose a number from 1 to 3, which translates to conservative, moderate, and aggresive. The client is also free to change allocation percentages in the monte carlo simulation, the years we simulate, and even include more than 5 equities if they desire. 

---

## Contributors

The contributors are Paul Lopez, Chaim Kriger, Isaac Iskra, Horayra Hossain

---

## License
No licenses required. Just get the consent of the contributors above and everything should be fine.
Chaim would like a tip :)