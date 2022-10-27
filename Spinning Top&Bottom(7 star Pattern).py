#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from nsepy import get_history
import datetime as DT
import pandas as pd
from datetime import date


def detect_spinning_pattern(df):
    df['BodyLength'] = (df['Close']-df['Open']).abs()
    df['HighLowGap'] = (df['High']-df['Low']).abs()
    df['WickLength'] = df['HighLowGap'] - df['BodyLength']
    if df['HighLowGap'].mean()*1.2 < df.tail(1).HighLowGap.values[0]:
        if df.tail(1).WickLength.values[0] > 2*df.tail(1).BodyLength.values[0] and (df.tail(1).Low.values[0]==df.Low.min() or df.tail(1).High.values[0]==df.High.max()):
            return 1
        else:
            return 0
    else:
        return 0    
    return 0

curr_date = DT.date.today() - DT.timedelta(days=15)
total_past_days = 365
start_date = curr_date - DT.timedelta(days=total_past_days)
two_week_ago = curr_date - DT.timedelta(days=14)

filePath = "C:\\Users\\adarsh.sandhu\\Downloads\\Market Data\\High Volume in daily chart\\StocksList.csv"
stockList = pd.read_csv(filePath)
while start_date!= curr_date:
    for i in stockList['symbol']:
        try:
            data = get_history(symbol=i, start=date(two_week_ago.year,two_week_ago.month,two_week_ago.day), end=date(curr_date.year,curr_date.month,curr_date.day))
            if data.Volume.mean()*1.5 < data.tail(1).Volume.values[0]:
                #print(i+"  "+str(curr_date))                
                if detect_spinning_pattern(data):
                    print("Spinning Pattern Detected in "+i+"on "+str(curr_date))
        except:
            print("Some exception occurred with symbol:-  "+i)
    curr_date = curr_date - DT.timedelta(days=1)
    two_week_ago = curr_date - DT.timedelta(days=14)
print("Completed Volume scan")


# In[24]:


import re
import pandas as pd
content = open(r"C:\Users\adarsh.sandhu\Downloads\Market Data\This_Year-Spinning Top&Bottom.txt",'r')
content_text = content.read()
content.close()
#print(content_text)
x = re.findall("Spinning\s*Pattern\s*Detected\s*in\s*([\w]+)on\s([\d\-]+)", content_text)
df = pd.DataFrame(x, columns=['Symbol', 'Date'])
df.to_csv("C:\\Users\\adarsh.sandhu\\Downloads\\Market Data\\This_Year-Spinning Top&Bottom.csv", index=False)


# In[21]:





# In[ ]:




