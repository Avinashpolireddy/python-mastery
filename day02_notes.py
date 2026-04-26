# Block A - Basic if/elif/else structure --

score =80

if score>=90:
    grade = "A"
elif score>=80:
    grade = "B"
elif score>70:
    grade = "C"
elif score>=60:
    grade = "D"
else:
    grade = "F"

print(f"score: {score}, grade: {grade}")

# Block B - comparison operators --
x= 15

print(x == 15) # Equal to
print(x != 15) # Not equal to
print(x > 10)  # Greater than
print(x < 20)  # Less than
print(x >= 15) # Greater than or equal to
print(x <= 15) # Less than or equal to

print(10 < x < 20) # Chained comparison
print( 0 <= x <= 100) # Check if x is between 0 and 100

# Block C - Boolean logic+ truththiness --

age = 25
has_id = True

if age > 20 and has_id:
    print("You can enter the club!")
if age <= 18 or not has_id:
    print("You cannot enter the club!")

# Block D - try/except for error handling --
try:
    age = int(input("Enter your age: "))
    print(f"Your age will be {age + 1} next year.")
except ValueError:
    print("Please enter a valid number for age.")

# Block E - match/case (Python 3.10+) --
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 301 | 302:
        print("Redirect")
    case 404:
        print("Not Found")
    case 500 | 502 | 503:
        print("Server Error")
    case _:
        print("Unknown")
