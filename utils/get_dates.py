# Last business day
# using pd.tseries.offsets.BusinessDay(n)
import pandas as pd
from datetime import datetime

  
  
#print(datetime.strptime('5/5/2019',
#                        '%d/%m/%Y')

def get_start_date():
    #today = date.today()
    
    # initializing dates
    test_today = datetime(2021, 7, 5)
    today = datetime.today()
  
    # printing original date
    #print("The original date is : " + str(today))
  
    # Creating Timestamp
    #ts = pd.Timestamp(str(today))
    #print(ts)
    # Create an offset of 1 Business days
    offset = pd.tseries.offsets.BusinessDay(n=1)
  
    # getting result by subtracting offset
    last_bday = today - offset
  
    # printing result
    #print("Last business day : " + str(last_bday))
    #start_date = pd.to_datetime(last_bday).dt.date
    start_date = last_bday.strftime("%m-%d-%Y")        
    #datetime.strptime(last_bday,'%d/%m/%Y')
    start_date = pd.Timestamp(start_date, tz = 'America/New_York').isoformat()
    
    return start_date


def get_end_date():
    #today = date.today()
    
    #prior = today + relativedelta(years=-5)
    
    #end_date = pd.Timestamp(prior, tz = 'America/New_York').isoformat()
    # initializing dates
    test_today = datetime(2021, 7, 5)
    today = datetime.today()
  
    # printing original date
    #print("The original date is : " + str(today))
  
    # Creating Timestamp
    #ts = pd.Timestamp(str(today))
  
    # Create an offset of 1 Business days
    offset = pd.tseries.offsets.BusinessDay(n=2650)
  
    # getting result by subtracting offset
    today_minus10yrs = today - offset
  
    # printing result
    #print("10 years ago : " + str(today_minus10yrs))
    end_date = today_minus10yrs.strftime("%m-%d-%Y") 
    end_date = pd.Timestamp(end_date, tz = 'America/New_York').isoformat()
    
    return end_date