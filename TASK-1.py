# 1. Print Hello World
print("Hello, World!")


# 2. Add two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)



# 3. Area of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
print("Area of rectangle:", length * width)




# 11. Check whether a number is positive, negative, or zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")





# 12. Check whether a year is a leap year
year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")




# 13. Calculate grade based on marks
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")


# 16. Print numbers from 1 to 100

for i in range(1, 101):
    print(i)



# 17. Print multiplication table of a given number

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)




# 32. Check whether a string is a palindrome

text = input("Enter a string: ")

# Convert to lowercase
text = text.lower()

# Reverse the string
reverse_text = text[::-1]

if text == reverse_text:
    print("Palindrome")
else:
    print("Not a Palindrome")



# 35. Find the largest element in a list

numbers = [10, 25, 7, 45, 18, 32]

largest = max(numbers)

print("Largest element:", largest)



# 41. Function to calculate factorial of a number

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))



# 49. Find the maximum value in a dictionary

data = {
    "A": 10,
    "B": 25,
    "C": 15,
    "D": 30
}

maximum = max(data.values())

print("Maximum value:", maximum)



# 52. Read the contents of a text file

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()




# 56. Handle division by zero using exception handling

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")