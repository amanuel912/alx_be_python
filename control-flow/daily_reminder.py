task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        base = 'a high priority task'
    case 'medium':
        base = 'a medium priority task'
    case 'low':
        base = 'a low priority task'

if time_bound == 'yes':
    print(f"Reminder: '{task}' is {base} that requires immediate attention today!")
else:
    print(f"Note: '{task}' is {base}. Consider completing it when you have free time.")
