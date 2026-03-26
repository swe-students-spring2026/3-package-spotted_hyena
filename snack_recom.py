import random 
def recommend_snack(mood,sweet_level):
    '''Recommends snacks based on sweet tooth level and mood'''
    
    if not (0<=sweet_level<= 10):
        raise ValueError("Sweet tooth has to be between 0-10.")
    mood= mood.lower()
    if mood not in ["happy", "stressed","sleepy"]:
        raise ValueError("Mood must be either happy, sleepy or stressed.")
    
    sweet_snacks= {
        "happy": ["cupcake", "ice cream", "bubble tea"],
        "stressed": ["brownie", "cookies", "chocolate bar"],
        "sleepy": ["pudding", "banana bread", "yogurt"]
    }
    salty_snacks= {
        "happy": ["popcorn", "pretzels", "fries"],
        "stressed": ["chips", "nachos","salted nuts"],
        "sleepy": ["crackers", "toast", "rice cakes"]
    }

    if sweet_level>= 7:
        return random.choice(sweet_snacks[mood])
    elif sweet_level<= 3:
        return random.choice(salty_snacks[mood])
    else:
        return random.choice(sweet_snacks[mood]+ salty_snacks[mood])