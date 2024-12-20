task = input("Enter your task: ")
pri = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

if time == "yes":
    print("Reminder: ",task, " is a ",pri, "priority task that requires immediate attention today!")

else:
    print("Reminder: ",task, " is a ",pri, "priority task. Consider completing it when you have free time.")