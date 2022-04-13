def getDistictNumberOfGcd(n):
    count = 0
    for i in range(1,n//2+1):
        if n % i == 0:
            count = count + 1
           
    return count + 1


print(getDistictNumberOfGcd(count))
