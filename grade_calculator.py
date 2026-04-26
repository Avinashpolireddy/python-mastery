# Ask the user for their name. If they enter nothing (empty string), print "Name cannot be empty." and exit.
name = input("Enter your name: ").strip()

if not name:
    print("Name cannot be empty.")
    exit()


# 2. Ask for a numeric score (0-100). 
# Handle these cases:Non-numeric input ("abc") → catch the ValueError, print "Score must be a number." and exit 
# Score below 0 or above 100 → print "Score must be between 0 and 100." and exit
try:
    score = float(input("Enter your score (0-100): "))
except ValueError:
    print("Score must be a number.")
    exit()
if score < 0 or score > 100:
    print("Score must be between 0 and 100.")   
    exit()

# 3. Calculate the letter grade based on the score using if/elif/else:
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# 4. Print a feedback message based on the grade:
match grade:
    case "A":
        feedback = "Excellent work!"
    case "B":
        feedback = "Great job!"
    case "C":
        feedback = "Solid effort."
    case "D":
        feedback = "You can do better."
    case "F":
        feedback = "Please see me after class."

print("========== GRADE REPORT ==========")
print(f"Student:  {name}")
print(f"Score:    {score} / 100")
print(f"Grade:    {grade}")
print(f"Feedback: {feedback}")
print("==================================")