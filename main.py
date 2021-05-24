# Time converter using Python

def TimeCon(num):
    minute = num % 6
    hours = int((num-minute)/60)
    timeconv = str(hours) + ":" + str(minute)
    return timeconv

print(TimeCon(60))
