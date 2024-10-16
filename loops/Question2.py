#question2

import random

moods = ['Happy', 'Sad', 'Energetic', 'Calm']
times = ['Morning', 'Afternoon', 'Evening']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
 
for i in range(len(days)):
    for t in range(len(times)):
        feeling = random.choice(moods)
        print(f"On {days[i]} {times[t]} you were feeling {feeling}.")