n = int(input("Enter the range of the number: "))
sum_even = 0


for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers is: ", sum_even)

# for i in range(2, n+1, 2):
#     sum_even += i

# print("The sum of even number upto n is:",sum_even)