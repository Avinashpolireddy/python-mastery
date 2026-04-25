# Day 1 Notes - Variables, Types, Operators, F-strings

# Block A -- Variable and Data Types -- 
name = "Avinash"
age = 35
hourly_rate = 165.50
is_contractor = True
nothing = None

print(name, age, hourly_rate, is_contractor, nothing)
print(type(name), type(age), type(hourly_rate), type(is_contractor), type(nothing))

# Block B -- Type Conversion -- 
age_str = "35"
age_num = int(age_str)
rate = float (165.50)
back_to_str = str(age_num)

print(age_num + 5)
print(rate * 2)
print(back_to_str + "!")

# Block C -- Operators -- 
print(10/5)  # Division
print(10//3) # Floor Division
print(10%3)  # Modulo
print(2**3)  # Exponentiation

x = 10
print(x>5 and x<15)  # Logical AND
print(x<5 or x>15)   # Logical OR
print(not(x==5))      # Logical NOT

# Block D -- F-strings --
name = "Avinash"
rate = 165.50
hours = 40

print(f"Hi {name}, you earned ${rate*hours} this week!")
print(f"earnings: ${rate*hours:.2f}")  # Format to 2 decimal places
print(f"earnings: ${rate*hours:,.2f}")  # Format with commas and 2 decimal places
print(f"name: {name:>15}")  # Right-align name in a field of width 15
print(f"name: {name:<15}")  # Left-align name in a field of width 15

# Block E -- string methods --
s = " Hello World! " 
print(s.strip())  # Remove leading and trailing whitespace
print(s.lower())  # Convert to lowercase
print(s.upper())  # Convert to uppercase
print(s.replace("World", "Python"))  # Replace substring
print("Hello".startswith("He"))  # Check if string starts with "He"
print("Hello".endswith("lo"))  # Check if string ends with "lo"
print("".join(["a,b,c"]))  # Join list of strings with a comma
print("a,b,c".split(","))  # Split string into a list using comma as separator
print(len(s))  # Get length of string
print(len("hello"))  # Get length of string

#Block F -- input() function --
your_name = input("enter you name: ")
your_age = input("enter your age: ")
print(f"Hello {your_name}, you are {your_age} years old!")
print(f"in 10 years, you will be {int(your_age) + 10} years old!")

