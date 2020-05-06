# Fibonacci works like this: 1 1 2 3 5 8 13 21 czyli bierze ostatnie dwie liczby i do siebie dodaje

# Moja metoda, ale tylko do liczby 34!
def fibo(num):
    list = [1, 1]
    i = 0
    j = 1
    k = list[i]
    l = list[j]
    for item in list:
        if i != num and num < 35:
            list.append(k + l)
            i += 1
            j += 1
            k = list[i]
            l = list[j]
    return list[num - 1]
#print(fibo(8))  # 34 to najwyzsza mozliwa


# Using recursion statement
nums = {}  # To musi byc tu, a nie w funkcji, bo inaczej bedzie sie wykonywac bardzo dlugo!
def Fibonacci(n):
    if n <= 2:
        return 1
    if n in nums:
        return nums[n]
    else:
        num = Fibonacci(n - 1) + Fibonacci(n - 2)
        nums[n] = num
        return num
print(Fibonacci())