import schedule
import time

def  main():
    print("1111")


schedule.every(4).seconds.do(main)
while 1:
    schedule.run_pending()
    