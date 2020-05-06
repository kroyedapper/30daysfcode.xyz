def primeSum(num):
    prime  = []
    sum = 0
    for num in range(2, num + 1):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:
                prime.append(num)
    for item in prime:
        sum+=item
    return sum

print(primeSum(10))
print(primeSum(20))
print(primeSum(100))

