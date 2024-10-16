#task1
import random

moods = ['Happy', 'Sad', 'Energetic', 'Calm']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for i in range(len(days)):
    feeling = random.choice(moods)
    print(f"On {days[i]} you were feeling {feeling}")

