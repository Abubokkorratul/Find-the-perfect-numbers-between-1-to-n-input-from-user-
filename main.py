n = int(input("Enter a number (n): "))
print("Perfect numbers between 1 and", n, ":")
for num in range(1, n + 1):
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == num:
        print(num, end=" ")
