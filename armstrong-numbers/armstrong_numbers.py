def is_armstrong(number):
    numberString = str(number)
    numberLength = len(numberString)
    numberList = list(numberString)
    sum = 0
    
    for num in numberList:
        sum += int(num) ** numberLength
    
    return sum == number