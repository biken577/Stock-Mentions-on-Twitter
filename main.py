from keep_alive import keep_alive
import time
import smtplib
import datetime
import time
from datetime import date
from datetime import datetime
import pytz
from pytz import timezone
from random import random
from replit import db
from csv import DictWriter
email_address="testingcode9413@gmail.com"
email_password="community1234$"
keep_alive()


from snscrape.modules.twitter import TwitterUserScraper,TwitterSearchScraper
import pandas as pd
from datetime import datetime

def twitteruserscraper(name):
  """
  search the user and provides its content
  """
  date=[]
  contents=[]
  users=[]
  
  for i,tweets in enumerate(TwitterUserScraper(name).get_items()):
    if i >50:
      break
    date.append(tweets.date)
    contents.append(tweets.content)
    users.append(tweets.user.username)
  df=pd.DataFrame({"Date":date,"Content":contents,"User":users})
  return df

#print(twitteruserscraper('elonmusk'))

def twittersearchscraper(search):
  """
  search the query and provides its content
  """
  date=[]
  contents=[]
  users=[]
  for i,tweets in enumerate(TwitterSearchScraper(search).get_items()):
    if i > 1000:
      break
    date.append(tweets.date)
    contents.append(tweets.content)
    users.append(tweets.user)
  df=pd.DataFrame({"Date":date,"Content":contents,"User":users},index=date)
  df.index=df.index.tz_convert('US/Central')
  return df




from csv import writer
from dateutil import tz
from datetime import timedelta

dt=timedelta(hours=1)
CT=tz.gettz('US/Central')
initial_hour=datetime.now(CT).hour
print("The initial hour is",initial_hour)

stock_list=["GME",'AMC',"NIO","TSLA","AAPL","NVDA",'RBLX','AMZN','HOOD','PLTR','PYPL','TWTR','XOM','COP']
stocks=[]
flag=True
while True:
    stocks=[]
    updated_time=datetime.now(CT)
    updated_hour=updated_time.hour
    print("The updated hour is",updated_hour)
    #if initial_hour!=updated_hour:
    
  
    if updated_hour==initial_hour+1:
      for stock in stock_list:
        df=twittersearchscraper("($"+str(stock)+" OR #"+str(stock)+ "OR "+str(stock)+")")
        lagged_time=updated_time-dt
        date_string=datetime.strftime(lagged_time,"%Y-%m-%d %H")
        stocks.append(len(df.loc[date_string]))
        
      with open('gme_hourly.csv','a',newline="") as f:
          writer_object=writer(f)
          writer_object.writerow([lagged_time,*stocks])
          f.close()
      initial_hour=initial_hour+1
      if initial_hour==23:
        initial_hour=-1
      print('The initial hour is set to',initial_hour)
      #time.sleep(3600)

# i=0

# central = timezone('US/Central')
# datetime_central=datetime.now(central)
# print(datetime_central)



# while True:
#   datetime_central=datetime.now(central)
#   print(datetime_central)
#   hours=datetime_central.strftime("%H")
#   mins=datetime_central.strftime("%M")
#   if hours=='13' and mins=='57':
#     with smtplib.SMTP('smtp.gmail.com',587) as smtp:
#       smtp.ehlo()
#       smtp.starttls()
#       smtp.ehlo()
      
#       smtp.login(email_address,email_password)
      
#       subject="grab dinner this weekend"
#       body="how about dinner at 6pm this saturday"
      
#       msg=f'Subject:{subject}\n\n{body}'
      
#       smtp.sendmail(email_address,email_address,msg)
#       print('Email is sent')
#       time.sleep(50)
#   i=i+1
#   print(i)
#   time.sleep(10)
# date_list=[]
# random_number=[]
# i=0
# while True:
#   date=datetime.now()
#   number1=random()
#   number2=random()
#   dict={"date":date,"number1":number1,"number2":number2}
#   i=i+1
#   print(i)
  
  # with open('CSVFILE.csv', 'a', newline='') as f_object:
  #   # Pass the CSV  file object to the Dictwriter() function
  #   # Result - a DictWriter object
  #   dictwriter_object = DictWriter(f_object, fieldnames=["date","number1","number2"])
  #   # Pass the data in the dictionary as an argument into the writerow() function
  #   dictwriter_object.writerow(dict)
  #   # Close the file object
  #   f_object.close()


  
  #time.sleep(30)

