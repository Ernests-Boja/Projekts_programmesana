import random

gym_krutis = ['bench press', 'dumbbell fly', 'chest press','decline push-ups','chest flys with cable machine']
gym_mugura = ['lat pulldowns', 'bent-over rows', 'seated cable rows','pull-ups','seated cable rows']
gym_kajas = ['leg press','barbell squats','walking lunges with dumbbells','romanian deadlifts with barbell','Leg curls with machine']
gym_rokas = ['bicep curls', 'tricep extensions', 'hammer curls', 'dips', 'skull crushers']
gym_prese = ['planks', 'crunches', 'Russian twists', 'sit-ups','hanging leg raises']

bez_gym_krutis = ['push-ups','wide push-ups','decline push-ups','pike push-ups']
bez_gym_mugura = ['pull-ups','chin-ups','Superman','cobra stretches','swimmer']
bez_gym_kajas = ['squats', 'lunges', 'deadlifts','calf raises','jump squats']
bez_gym_rokas = ['push-ups','dips','tricep dips on bench or chair','diamond push-ups','weighted arm curls']
bez_gym_prese = ['planks', 'crunches', 'Russian twists', 'sit-ups','mountain climbers']

ilgums = {'15min': (8, 12), '30min': (12, 15), '60min': (15, 20)}

ekipejums = input("Vai vēlaties trenēties sporta zālē (ar aprīkojumu) vai bez aprīkojuma? Ievadi 'ar' vai 'bez' -  ")

kermena_dala = input('Kuru ķermeņa daļu vēlaties trenēt? (krūtis, mugura, kājas, rokas vai prese) - ')

trenina_ilgums = input('Cik ilgi vēlies trenēties? (15min , 30min , or 60min) - ')

min_atkartojums, max_atkartojums = ilgums[trenina_ilgums]

if ekipejums == 'ar':
    if kermena_dala == 'krūtis':
        for i in range (3):
            uzdevums = random.choice(gym_krutis)
            print(f"Izpildi {uzdevums} {random.randint(min_atkartojums, max_atkartojums)} reizes.")       
    elif kermena_dala == 'mugura':
        for i in range (3):
            uzdevums = random.choice(gym_mugura)
            print(f"Izpildi {uzdevums} {random.randint(min_atkartojums, max_atkartojums)} reizes.")      
    elif kermena_dala == 'kājas':
        for i in range (3):
            uzdevums = random.choice(gym_kajas)
            print(f"Izpildi {uzdevums} {random.randint(min_atkartojums, max_atkartojums)} reizes.")        
    elif kermena_dala == 'rokas':
        for i in range (3):
            uzdevums = random.choice(gym_rokas)
            print(f"Izpildi {uzdevums} {random.randint(min_atkartojums, max_atkartojums)} reizes.")       
    elif kermena_dala == 'prese':
        for i in range (3):
            uzdevums = random.choice(gym_prese)
            print(f"Izpildi {uzdevums} {random.randint(min_atkartojums, max_atkartojums)} reizes.")
    else:
        print("Nepareizi ievadīta ķermeņa daļa.")
        
elif ekipejums == 'bez':
    if kermena_dala == 'krūtis':
        for i in range (3):
            uzdevums = random.choice(bez_gym_krutis)
            print(f"Izpildi {uzdevums} {random.randint(min_atkartojums, max_atkartojums)} reizes.")       
    elif kermena_dala == 'mugura':
        for i in range (3):
            uzdevums = random.choice(bez_gym_mugura)
            print(f"Izpildi {uzdevums} {random.randint(min_atkartojums, max_atkartojums)} reizes.")       
    elif kermena_dala == 'kājas':
        for i in range (3):
            uzdevums = random.choice(bez_gym_kajas)
            print(f"Izpildi {uzdevums} {random.randint(min_atkartojums, max_atkartojums)} reizes.")        
    elif kermena_dala == 'rokas':
        for i in range (3):
            uzdevums = random.choice(bez_gym_rokas)
            print(f"Izpildi {uzdevums} {random.randint(min_atkartojums, max_atkartojums)} reizes.")
    elif kermena_dala == 'prese':
        for i in range (3):
            uzdevums = random.choice(bez_gym_prese)
            print(f"Izpildi {uzdevums} {random.randint(min_atkartojums, max_atkartojums)} reizes.")
    else:
        print("Nepareizi ievadīta ķermeņa daļa.")    