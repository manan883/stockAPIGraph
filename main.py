from polygon import RESTClient
import matplotlib.pyplot as plt
import datetime
from dateutil.relativedelta import relativedelta
client = RESTClient("glC4xoO2asbJu8Wh4DJ0Y2x6fo2w0IJN")




#this gets the close data as a float 
# aggs = client.get_aggs("SPY", 1, "day", "2022-04-04", "2022-04-04")
# x = (str(aggs[0]).split("="))
# y = (x[4])
# z = y.split(",")
# print(float(z[0]))
#end close data as float 


#make the aggs arguemntable 
while True:
    choice = input("Press c to chart a stock and any other key to exit: ")
    match choice.lower():
        case "c":
            ticker = input("enter the stock symbol to chart: ")
            ticker = ticker.upper()
            from_ = str(datetime.datetime.today() - relativedelta(years=1)).split()[0]
            to = str(datetime.datetime.today()).split()[0]
            try:
                aggs = client.get_aggs(ticker, 1, "day", from_, to)
                counter = 4
                closeData = []
                try:
                    for i in range(600):
                        x = (str(aggs).split("="))
                        y = (x[counter])
                        z = y.split(",")
                        closeData.append(float(z[0]))
                        counter+=9
                except:
                    pass
                plt.plot(closeData)
                plt.xlabel("Number of days")
                plt.ylabel("Price")
                plt.title(ticker)
                plt.show() 
            except:
                print("INVALID SYMBOL")
        case other:
            break

    # print(str(aggs).split("="))
    
# print(str(datetime.datetime.today()).split()[0])





'''
4 for the first close 
13 for the second close
22 for the third close 
171.83
'''

