task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time == "yes":
            print("Reminder: ",task, " is a ",priority, "priority task that requires immediate attention today!")
    case "medium":
        if time == "yes":
            print("Reminder: ",task, " is a ",priority, "priority task that requires immediate attention today!")
    case "low":
        print("Reminder: ",task, " is a ",priority, "priority task. Consider completing it when you have free time.")





