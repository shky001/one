
import datetime
import time as t

def date():
    print(f"当前的日期为{datetime.date.today()}")

def time():
    print(f"当前的时间为{t.strftime('%H:%M:%S')}")

if __name__=="__main__":
    date()
    time()



