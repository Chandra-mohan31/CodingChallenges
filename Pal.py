# def isPalindrome(x):
#     y = 0


#     while x != 0:

#         y = y*10 + x%10

#         x = x/10
#     print(y)
# isPalindrome(121)

# Ask for enter the number from the use
number = int(input("Enter the integer number: "))

# Initiate value to null
test = number
revs_number = 0

# reverse the integer number using the while loop

while (number > 0):
    # Logic
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10

# Display the result

print(test)

print("The reverse number is : {}".format(revs_number))
