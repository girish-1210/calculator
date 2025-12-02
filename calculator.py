# GitHub Activity Planner

print("=== GitHub Activity Planner ===")

# User input for goal
goal_commits = int(input("Aap mahine me kitne commits ka target rakhna chahte ho? : "))
working_days = int(input("Aap mahine me kitne din coding karenge? : "))

# Calculate commits per day
if working_days == 0:
    print("Working days zero nahi ho sakte!")
else:
    commits_per_day = goal_commits / working_days

    print("\n--- Activity Plan ---")
    print(f"Monthly Commit Goal: {goal_commits}")
    print(f"Working Days: {working_days}")
    print(f"Required Commits Per Day: {commits_per_day:.2f}")

    if commits_per_day <= 1:
        print("Plan: Easy ⭐ — Daily 1 commit se goal poora ho jayega.")
    elif commits_per_day <= 3:
        print("Plan: Moderate ⚡ — Kaafi manageable schedule hai.")
    else:
        print("Plan: Hard 🔥 — Coding routine improve karne ki zarurat hogi!")