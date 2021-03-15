import time


def factorial(num):
    global fact_count
    fact_count += 1
    if num <= 1:
        return 1
    return num * factorial(num - 1)


num = int(input("Enter a non negative number: "))
fact_count = 0
start = time.time()
factorial(num)
stop = time.time()
print("The answer is", factorial(num))
print("The number of function calls is", fact_count)
print("The time taken is", stop - start)