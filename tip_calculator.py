
Bill = float(input(" Bill : $"))
tip_percentage = float(input(" tip percentage : $"))
number_of_people = int(input("Number of people : "))

Tip = Bill * (tip_percentage / 100)
Total = Bill + Tip
per_person = Total / number_of_people

print("========== Receipt ==========")
print(f"bill: ${Bill:.2f}")
print(f"tip:  ${Tip:.2f}")
print(f"total: ${Total:.2f}")
print(f"per person:  ${per_person:.2f}")
print("=============================")
