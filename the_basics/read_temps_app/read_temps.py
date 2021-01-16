import pandas #is a fast, powerful, flexible and easy to use open source data analysis 
import os
import time


while True:
    if os.path.exists('../files/temps_today.csv'):
       data = pandas.read_csv("../files/temps_today.csv")
       print(data.mean()['st2'])
    else:
        print('Not Found')
    time.sleep(5)