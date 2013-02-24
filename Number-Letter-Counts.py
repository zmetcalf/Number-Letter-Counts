#Solved but can be short

Counter = 1
total = 0

def oneThroughNine(num):
    if(num == 1):
        return 3
    elif(num == 2):
        return 3
    elif(num == 3):
        return 5
    elif(num == 4):
        return 4
    elif(num == 5):
        return 4
    elif(num == 6):
        return 3
    elif(num == 7):
        return 5
    elif(num == 8):
        return 5
    elif(num == 9):
        return 4
    
def teens(num):
    if(num == 10):
        return 3
    elif(num == 11):
        return 6
    elif(num == 12):
        return 6
    elif(num == 13):
        return 8
    elif(num == 14):
        return 8
    elif(num == 15):
        return 7
    elif(num == 16):
        return 7
    elif(num == 17):
        return 9
    elif(num == 18):
        return 8
    elif(num == 19):
        return 8

def doubleDigit(num):
    tempNum = (int(num / 10))
    yNum = 0
    
    if(tempNum == 2):
        yNum = 6
    elif(tempNum == 3):
        yNum =  6
    elif(tempNum == 4):
        yNum = 5
    elif(tempNum == 5):
        yNum = 5
    elif(tempNum == 6):
        yNum = 5
    elif(tempNum == 7):
        yNum = 7
    elif(tempNum == 8):
        yNum = 6
    elif(tempNum == 9):
        yNum =  6
        
    if (num % 10 != 0):
        yNum = yNum + oneThroughNine((num - (tempNum * 10)))
    return yNum
    
for x in range(1, 1000):    
    counter = x
    if(counter >= 100):
        if(counter % 100 != 0): # adds "and"
            total = total + 3
        total = total + oneThroughNine(int(counter / 100)) + 7
        counter = counter - (int(counter/100) * 100)
    if(counter >= 20):
        total = total + doubleDigit(counter)   
    elif(counter >= 10 and counter < 20):
        total = total + teens(counter)  
    elif(counter < 10 and counter != 0):
        total = total + oneThroughNine(counter)

total = total + 11 # one thousand

print total
