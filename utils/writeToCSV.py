import csv
from pathlib import Path

def writeToCSV(fileName1, dataframe1): #for Chaim if he wants to combine it

   
        dataframe1.to_csv(fileName1, index=False)
        
        
        print("Reports have been saved. Have a nice day!")



