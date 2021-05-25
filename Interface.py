import database
from tkinter import *
from tkinter.messagebox import showinfo
import json
import requests
# import schedule
import time
import sys
import datetime 
import sqlite3
#//// connection
connection = database.connect()
database.create_table(connection)
#//////////////
window = Tk()
window.title("Crypto_Currency")
window.geometry('400x200')
##//////// 
period_id = Label(window, text="Time frame")
period_id.grid(column=0, row=0)

limit5 = Label (window, text="limit for 5 candels")
limit5.grid(column=0, row=1)

limit10 = Label (window, text="limit for 10 candels")
limit10.grid(column=0, row=2)

limit20 = Label (window, text="limit for 20 candels")
limit20.grid(column=0, row=3)


#_period_id = Entry (window , width=10)
#_period_id.grid(column=1, row=0)

_limit5 = Entry (window , width=10 )
_limit5.grid (column=1, row=1) 

_limit10 = Entry (window , width= 10)
_limit10.grid (column=1, row=2)

_limit20 = Entry (window , width= 10)
_limit20.grid (column=1, row=3)


symbol_array = ["BTC/USDT","ETH/USDT"]
array_length = len(symbol_array)
which_crypto =[]
parameters = {
    "secret": "Get Key from https://taapi.io/",
    "construct": 
    {
        "exchange": "binance",
        "symbol": "BTC/USDT",
        "interval": "5m",
        "indicators": 
        [
            {
                "indicator": "tema",
                "optInTimePeriod" : 5
            },
            {
                "indicator": "tema",
                "optInTimePeriod" : 10
            },
            {
                "indicator": "tema",
                "optInTimePeriod" : 20
            }
        ]
    }
}
###//// Def Func
def clicked():
    b='1'
    while (1):
        if (b=='1'):
            for i in range(array_length):
                print("-----------------------------------------------------")
                parameters["construct"]["interval"]="5m"
                parameters["construct"]["symbol"]=symbol_array[i]
                parameters["construct"]["indicators"][0]["optInTimePeriod"] = _limit5.get()
                parameters["construct"]["indicators"][1]["optInTimePeriod"] = _limit10.get()
                parameters["construct"]["indicators"][2]["optInTimePeriod"] = _limit20.get()
                # Send get request and save the response as response object 
                endpoint = "https://api.taapi.io/bulk"
                status_code_condition = True
                while status_code_condition:
                     
                    try:
                        response = requests.post(url = endpoint, json = parameters)
                        
                        if (response.status_code ==200):
                            print("connection is on ------>interval=5m")
                            result = response.json()
                            status_code_condition = False
                        else:
                            time.sleep(5)
                    except:
                        time.sleep(5)
                    
                #/////////////
                
                #try :
                    # Extract data in json format 
                    #result = response.json() 
                #except ValueError:
                    #print("Response content is not valid JSON")
                print("TEMA :",parameters["construct"]["symbol"])
                print("5:",result["data"][0]["result"]["value"])
                print("10",result["data"][1]["result"]["value"])
                print("20",result["data"][2]["result"]["value"])
                temp5=result["data"][0]["result"]["value"]
                temp10=result["data"][1]["result"]["value"]
                temp20=result["data"][2]["result"]["value"]
                #print(temp5)
                #print(temp10)
                #print(temp20)
                if(temp5<=temp10):
                    print("temp5<=temp10")
                    x1=temp5/temp10
                elif(temp5>=temp10):
                    print("temp5>=temp10")
                    x1=temp10/temp5 
                if(temp10<=temp20):
                    print("temp10<=temp20")
                    x2=temp10/temp20
                elif(temp10>=temp20):
                    print("temp10>=temp20")
                    x2=temp20/temp10
                #/// way1
                #z1=float(f'{x1:.06f}'[:-4])
                #z2=float(f'{x2:.06f}'[:-4])
                #/// way2
                str1=str(x1)
                str2=str(x2)
                z1=float(str1[:str1.find('.')+5])
                z2=float(str2[:str1.find('.')+5])
                #// way3
                #z1=int(x1*1000)
                #z2=int(x2*1000)
                print("x1",x1," z1",z1)
                print("x2",x2," z2",z2)
                if((z1>=0.9998) and (z1<=1) and (z2>=0.9998) and (z2<=1)):
                    #showinfo ("Alert" ,parameters["construct"]["symbol"])
                    print("i found someting ....................................")
                    current_time = datetime.datetime.now() 
                    which_crypto.append((symbol_array[i],temp5,temp10,temp20,current_time))
                    Name=symbol_array[i]
                    Tema5=temp5
                    Tema10=temp10
                    Tema20=temp20
                    Time=current_time
                    TimeFrame="5m"
                    database.add_test(connection,Name,Tema5,Tema10,Tema20,Time,TimeFrame)
                else :
                    print("Wrong")
            b='0'
        else:
            for i in range(array_length):
                print("-----------------------------------------------------")
                parameters["construct"]["interval"]="4h"
                parameters["construct"]["symbol"]=symbol_array[i]
                parameters["construct"]["indicators"][0]["optInTimePeriod"] = _limit5.get()
                parameters["construct"]["indicators"][1]["optInTimePeriod"] = _limit10.get()
                parameters["construct"]["indicators"][2]["optInTimePeriod"] = _limit20.get()
                # Send get request and save the response as response object 
                endpoint = "https://api.taapi.io/bulk"
                status_code_condition = True
                while status_code_condition:
                     
                    try:
                        response = requests.post(url = endpoint, json = parameters)
                        
                        if (response.status_code ==200):
                            print("connection is on ------>interval=4h")
                            result = response.json()
                            status_code_condition = False
                        else:
                            time.sleep(5)
                    except:
                        time.sleep(5)
                #try :
                    # Extract data in json format 
                    #result = response.json() 
                #except ValueError:
                    #print("Response content is not valid JSON")
                print("TEMA :",parameters["construct"]["symbol"])
                print("5:",result["data"][0]["result"]["value"])
                print("10",result["data"][1]["result"]["value"])
                print("20",result["data"][2]["result"]["value"])
                temp5=result["data"][0]["result"]["value"]
                temp10=result["data"][1]["result"]["value"]
                temp20=result["data"][2]["result"]["value"]
                #print(temp5)
                #print(temp10)
                #print(temp20)
                if(temp5<=temp10):
                    print("temp5<=temp10")
                    x1=temp5/temp10
                elif(temp5>=temp10):
                    print("temp5>=temp10")
                    x1=temp10/temp5 
                if(temp10<=temp20):
                    print("temp10<=temp20")
                    x2=temp10/temp20
                elif(temp10>=temp20):
                    print("temp10>=temp20")
                    x2=temp20/temp10
                #/// way1
                #z1=float(f'{x1:.06f}'[:-4])
                #z2=float(f'{x2:.06f}'[:-4])
                #/// way2
                str1=str(x1)
                str2=str(x2)
                z1=float(str1[:str1.find('.')+5])
                z2=float(str2[:str1.find('.')+5])
                #// way3
                #z1=int(x1*1000)
                #z2=int(x2*1000)
                print("x1",x1," z1",z1)
                print("x2",x2," z2",z2)
                if((z1>=0.9998) and (z1<=1) and (z2>=0.9998) and (z2<=1)):
                    #showinfo ("Alert" ,parameters["construct"]["symbol"])
                    print("i found someting ....................................")
                    current_time = datetime.datetime.now() 
                    which_crypto.append((symbol_array[i],temp5,temp10,temp20,current_time))
                    Name=symbol_array[i]
                    Tema5=temp5
                    Tema10=temp10
                    Tema20=temp20
                    Time=current_time
                    TimeFrame="4h"
                    database.add_test(connection,Name,Tema5,Tema10,Tema20,Time,TimeFrame)
                else :
                    print("Wrong")
            b='1'
            
def stop():
    sys.exit()      
###/////////////////
sell_buy = Button (window , text="Which Crypto ? ",command= clicked)
sell_buy.grid(column=2, row=2)

stop = Button (window , text="Stop ",command= stop)
stop.grid(column=3, row=2)

window.mainloop()

