import schedule
import time

#  functions set up
def test1():
    print("this is a test")


#  task scheduling
schedule.every(2).minutes.do(test1)

#  Loop so that the scheduling task keep running all the time
while True:

    #  checks whether a scheduled task is pending or not
    schedule.run_pending()
    time.sleep(1)