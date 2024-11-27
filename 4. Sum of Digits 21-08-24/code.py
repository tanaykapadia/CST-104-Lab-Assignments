def sum_of_digits (n):
    if n == 0:
        return 0
    else:
        return ((n % 10) + sum_of_digits(n // 10))

print("Enter your number:")
n = int(input())
print("The sum of the digits of your number is:")
print(sum_of_digits(n))