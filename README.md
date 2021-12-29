# Machine Learning Trading Bot Application

Our portfolio analysis application can be used by anyone looking to invest over one million dollars into a portfolio. The goal of this application is to provide our user with data analytics that can help the user decide the time horizon he/she would like to invest for.

The application will ask the user for the amount they would like to invest, and for the user's risk tolerence. Our team has custom made 3 seperate baskets of  equities based on different levels of risk so we can provide a portfolio tailored to the user's preference.

Each basket contains 5 equities, and the application will use a formula to assign weights for each of the equities in an attempt to produce the maximum amount of returns for our user.

The application uses Monte Carlo Simulations to give the user an idea of how their portfolio might look at the end of their holding period by showcasing a lower and upper bound prediction using a 95% confidence interval.

Our Monte Carlo Simulations run for three different time periods: 5 years, 10 years, and 20 years.

With the results of our simulations, the application will output a csv file with all the user's information. This report will include the portfolio value, the equities in the portfolio, the amount of shares per equity, the value assigned to each equity, and the 3 Monte Carlo Simulations with their lower and upper bound prediction using a 95% confidence interval.

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

To use the application, launch jupyter lab from the gitbash terminal and run the 'portfolio_analysis.ipynb' noteback from the 
webpage. Ensure the 'MCForecastTools.py' file, 'gitignore' file, and '.env' files are in the directory where you run 'portfolio_analysis.ipynb'.
The user will be asked to input a portfolio amount, and their risk tolerence. The user will be asked to choose a number from 1 to 3, which translates to conservative, moderate, and aggresive. The client is also free to change allocation percentages in the monte carlo simulation, the years we simulate, and even include more than 5 equities if they desire. 

---

## Contributors


The contributors are Paul Lopez, Chaim Kriger, Bipasha Goswami, Briggs Lalor, and Nev Douglas

---

## License
No licenses required. Just get the consent of the contributors above and everything should be fine.
Chaim would like a tip :)