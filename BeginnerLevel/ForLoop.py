#5.For loop

import random
# 1. Simulate rolling a six-sided die 20 times
def roll_die():
    rolls = []  # Store all rolls
    count_6 = 0  # Count how many times 6 is rolled
    count_1 = 0  # Count how many times 1 is rolled
    consecutive_6 = 0  # Count how many times two 6s are rolled in a row
    for _ in range(20):  # Roll the die 20 times
        roll = random.randint(1, 6)  # Random number between 1 and 6
        rolls.append(roll)
        if roll == 6:
            count_6 += 1
        elif roll == 1:
            count_1 += 1
        # Check for two 6s in a row
        if len(rolls) >= 2 and rolls[-1] == 6 and rolls[-2] == 6:
            consecutive_6 += 1
    print(f"Rolls: {rolls}")
    print(f"Number of times 6 was rolled: {count_6}")
    print(f"Number of times 1 was rolled: {count_1}")
    print(f"Number of times two 6s were rolled in a row: {consecutive_6}")

# 2. Create a workout routine for 100 jumping jacks
def workout_routine():
    total_jumping_jacks = 100
    jumping_jacks_done = 0
    while jumping_jacks_done < total_jumping_jacks:
        print(f"Do 10 jumping jacks. Remaining: {total_jumping_jacks - jumping_jacks_done}")
        jumping_jacks_done += 10
        if jumping_jacks_done >= total_jumping_jacks:
            print("Congratulations! You completed the workout.")
            break
        tired = input("Are you tired? (yes/no): ").strip().lower()
        if tired in ["yes", "y"]:
            skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
            if skip in ["yes", "y"]:
                print(f"You completed a total of {jumping_jacks_done} jumping jacks.")
                break
# Run the functions
print("Task 1: Rolling a Die 20 Times")
roll_die()

print("\nTask 2: Workout Routine")
workout_routine() 
