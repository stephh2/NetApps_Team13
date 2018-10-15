import datetime

def getTimeStamp() :
    return str(datetime.datetime.now()).split('.')[0].split(' ')[1]