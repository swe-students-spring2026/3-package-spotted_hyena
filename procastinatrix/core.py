import random

ENCOURAGEMENTS = [
  "You're doing better than you think.",
  "Keep going — progress is happening.",
  "Small steps still move you forward.",
  "You've overcome hard things before.",
  "It's okay to take things one step at a time.",
  "You don't need to be perfect to be making progress.",
  "Every effort you make counts.",
  "You're learning, even when it feels slow.",
  "You've got this.",
  "The fact that you're trying matters."
]

QUICK_ACTIVITIES = [
    "Do 20 pushups or stretch",
    "Step outside for fresh air",
    "Clean your desk",
    "Write down 3 things on your mind",
    "Listen to one song without distractions",
    "Drink water and reset"
]

PRODUCTIVE_ACTIVITIES = [
    "Read a few pages of a book",
    "Watch a short educational video",
    "Review class notes",
    "Write a journal entry",
    "Plan your next day",
    "Solve one coding problem"
]

CREATIVE_ACTIVITIES = [
    "Take photos around your area",
    "Write a short story",
    "Sketch something random",
    "Build a small coding feature",
    "Make a playlist based on a mood"
]

SOCIAL_ACTIVITIES = [
    "Call or text a friend",
    "Go for a walk in a busy area",
    "Sit in a café and people-watch",
    "Play a quick game with someone"
]

RESET_ACTIVITIES = [
    "Take a short nap",
    "Go for a walk without your phone",
    "Sit quietly for 5-10 minutes",
    "Do nothing intentionally"
]

def instructions():
   return ("Functions" \
   "1. motivation(): Returns words of encouragement"
   "2. fake_productivity(): Asks type of activity you are interested in and returns an activity based on your type")

def motivation():
  return random.choice(ENCOURAGEMENTS) 

def fake_productivity():
  activity_arr = ["1. Quick Activity", "2. Productive Activity", "3. Creative Activity", "4. Social Activity", "5. Reset Activity"]
  for choice in activity_arr:
    print(choice)
  activity = int(input(("Choose which type of activity you would want?")))
  if activity>5:
    print("Enter a valid number")
    fake_productivity()
  elif activity == 1:
      return random.choice(QUICK_ACTIVITIES)
  elif activity == 2:
      return random.choice(PRODUCTIVE_ACTIVITIES)
  elif activity == 3:
      return random.choice(CREATIVE_ACTIVITIES)
  elif activity == 4:
      return random.choice(SOCIAL_ACTIVITIES)
  elif activity == 5:
      return random.choice(RESET_ACTIVITIES)

# need to intall wheel, sdist, pytest
  
# Function 2 snack recommender
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

#Function 3 break time
def break_excuse(deadline):
    #Gives you a length of time to take a break for
    #Deadline : time in minutes until deadline
    if not (0 < deadline):
        raise ValueError("Deadline has already passed.")
   
    if (deadline <= 60): return "You don't have time for a break, get to work!"
    elif (60 < deadline <= 120): return "You can take a 5-10 minute break, make sure to set a timer!"
    elif (120 < deadline <= 240): return "You can take a 10-15 minute break, make sure to set a timer!"
    elif (240 < deadline <= 480): return "You can take a 20-30 minute break, make sure to set a timer!"
    elif (480 < deadline <= 1440): return "No rush, take an hour long break, or a few 15 minute breaks."
    elif (1440 < deadline): return "It's not due until tomorrow, you have time, get back to it later!"

#Function 4 procrastination plan
def procrastination_plan(task, urgency, guilt_level):
    #Returns a procrastination strategy based on urgency and guilt level.
    if not task or not isinstance(task, str):
        raise ValueError("Task must be a non-empty string.")
    if not (0 <= urgency <= 10):
        raise ValueError("Urgency must be between 0 and 10.")
    if not (0 <= guilt_level <= 10):
        raise ValueError("Guilt level must be between 0 and 10.")

    if urgency >= 6 and guilt_level >= 6:
        return f"Open {task}, review what needs to be done, and complete one small part to get started."
    elif urgency >= 6:
        return f"You should begin {task} soon. Consider taking a short reset, then start immediately."
    elif guilt_level >= 6:
        return f"If {task} is weighing on you, open it and make some visible progress, even if it is small."
    else:
        return f"Set a clear start time for {task} and commit to beginning when that time arrives."

#Function 5 snack reward
def motivation_line(snack, task):
    #Returns a motivational line using a snack reward.
    if not snack or not isinstance(snack, str):
        raise ValueError("Snack must be a non-empty string.")
    if not task or not isinstance(task, str):
        raise ValueError("Task must be a non-empty string.")

    return f"Complete {task}, and you can reward yourself with {snack}."

#Function 6 return to woek
def return_to_work_message(task, break_length):
    #Returns a message encouraging you to return to your task.
    if not task or not isinstance(task, str):
        raise ValueError("Task must be a non-empty string.")
    if break_length < 0:
        raise ValueError("Break length cannot be negative.")

    if break_length <= 10:
        return f"Your break is complete. It is time to return to {task}."
    elif break_length <= 30:
        return f"You've had a long break. Get back to working on {task}."
    else:
        return f"You have been away for a while. Get started with {task} and move it forward."