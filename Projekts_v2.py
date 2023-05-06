import random

# Define the different drills for each body part that require equipment
gym_chest_drills = ['bench press', 'dumbbell fly', 'chest press','decline push-ups','chest flys with cable machine']
gym_back_drills = ['lat pulldowns', 'bent-over rows', 'seated cable rows','pull-ups','seated cable rows']
gym_leg_drills = ['leg press','barbell squats','walking lunges with dumbbells','romanian deadlifts with barbell','Leg curls with machine']
gym_arm_drills = ['bicep curls', 'tricep extensions', 'hammer curls', 'dips', 'skull crushers']
gym_core_drills = ['planks', 'crunches', 'Russian twists', 'sit-ups','hanging leg raises']

# Define the different drills for each body part that don't require equipment
no_gym_chest_drills = ['push-ups','wide push-ups','decline push-ups','pike push-ups']
no_gym_back_drills = ['pull-ups','chin-ups','Superman','cobra stretches','swimmer']
no_gym_leg_drills = ['squats', 'lunges', 'deadlifts','calf raises','jump squats']
no_gym_arm_drills = ['push-ups','dips','tricep dips on bench or chair','diamond push-ups','weighted arm curls']
no_gym_core_drills = ['planks', 'crunches', 'Russian twists', 'sit-ups','mountain climbers']

# Define the duration of each workout and the corresponding rep range for each drill
duration = {'15min': (8, 12), '30min': (12, 15), '1h': (15, 20)}

# Prompt the user to select whether they want to train with or without equipment
equipment_choice = input("Do you want to train at the gym (with equipment) or without equipment? Enter 'gym' or 'no gym': ")

# Prompt the user to select which body part they want to train
body_part = input('Which body part do you want to train? (chest, back, legs, arms, or core): ')

# Prompt the user to select the duration of their workout
workout_duration = input('How long do you want to train? (15min , 30min , or 1h): ')

# Determine the rep range for each drill based on the workout duration
min_reps, max_reps = duration[workout_duration]

# Select a random drill for the chosen body part based on whether the user wants to train with or without equipment, and print the number of reps
if equipment_choice == 'gym':
    if body_part == 'chest':
        for i in range (3):
            drill = random.choice(gym_chest_drills)
            print(f"Perform {random.randint(min_reps, max_reps)} reps of {drill}.")       
    elif body_part == 'back':
        for i in range (3):
            drill = random.choice(gym_back_drills)
            print(f"Perform {random.randint(min_reps, max_reps)} reps of {drill}.")       
    elif body_part == 'legs':
        for i in range (3):
            drill = random.choice(gym_leg_drills)
            print(f"Perform {random.randint(min_reps, max_reps)} reps of {drill}.")        
    elif body_part == 'arms':
        for i in range (3):
            drill = random.choice(gym_arm_drills)
            print(f"Perform {random.randint(min_reps, max_reps)} reps of {drill}.")       
    elif body_part == 'core':
        for i in range (3):
            drill = random.choice(gym_core_drills)
            print(f"Perform {random.randint(min_reps, max_reps)} reps of {drill}.")
    else:
        print("Invalid body part.")
        
elif equipment_choice == 'no gym':
    if body_part == 'chest':
        for i in range (3):
            drill = random.choice(no_gym_chest_drills)
            print(f"Perform {random.randint(min_reps, max_reps)} reps of {drill}.")       
    elif body_part == 'back':
        for i in range (3):
            drill = random.choice(no_gym_back_drills)
            print(f"Perform {random.randint(min_reps, max_reps)} reps of {drill}.")       
    elif body_part == 'legs':
        for i in range (3):
            drill = random.choice(no_gym_leg_drills)
            print(f"Perform {random.randint(min_reps, max_reps)} reps of {drill}.")        
    elif body_part == 'arms':
        for i in range (3):
            drill = random.choice(no_gym_arm_drills)
            print(f"Perform {random.randint(min_reps, max_reps)} reps of {drill}.")
    elif body_part == 'core':
        for i in range (3):
            drill = random.choice(no_gym_core_drills)
            print(f"Perform {random.randint(min_reps, max_reps)} reps of {drill}.")
    else:
        print("Invalid body part.")    