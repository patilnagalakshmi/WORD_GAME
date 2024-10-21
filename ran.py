# from random_word import RandomWords

# r = RandomWords()

# try:
#     # Generate a random word that has a dictionary definition and fits the criteria
#     word = r.get_random_word(hasDictionaryDef="true", 
#                              includePartOfSpeech="noun,verb", 
#                              minCorpusCount=1, 
#                              maxCorpusCount=10, 
#                              minDictionaryCount=1, 
#                              maxDictionaryCount=10, 
#                              minLength=5, 
#                              maxLength=10)

#     print(f"Generated Word: {word}")
    
# except Exception as e:
#     print(f"An error occurred: {e}")


import random 
words_list = [
    "Abandon", "Achieve", "Adapt", "Admire", "Advise", "Agree", "Aim", "Allow", "Apologize", "Appear",
    "Approach", "Approve", "Arrange", "Arrive", "Ask", "Attack", "Avoid", "Bake", "Balance", "Bathe",
    "Begin", "Believe", "Borrow", "Break", "Breathe", "Build", "Burn", "Call", "Capture", "Celebrate",
    "Change", "Charge", "Chase", "Choose", "Climb", "Close", "Collect", "Comfort", "Communicate", "Compare",
    "Complain", "Complete", "Concentrate", "Confirm", "Connect", "Consider", "Consult", "Contain", "Continue", "Correct",
    "Able", "Abundant", "Accurate", "Active", "Actual", "Acute", "Afraid", "Alert", "Alive", "Ambitious",
    "Angry", "Anxious", "Ashamed", "Attractive", "Average", "Awake", "Basic", "Beautiful", "Bitter", "Brave",
    "Bright", "Brilliant", "Broken", "Busy", "Calm", "Capable", "Careful", "Certain", "Charming", "Cheerful",
    "Clear", "Clever", "Close", "Cold", "Comfortable", "Confident", "Confused", "Content", "Cool", "Crazy",
    "Cruel", "Curious", "Dangerous", "Dark", "Dead", "Dear", "Deep", "Delicious", "Dense", "Dependent","Defend", "Delay", "Deliver", "Deny", "Depend", "Describe", "Destroy", "Develop", "Devote", "Direct",
    "Discover", "Discuss", "Dislike", "Display", "Divide", "Draw", "Dream", "Dress", "Drink", "Drive",
    "Drop", "Eat", "Encourage", "Enjoy", "Enter", "Escape", "Examine", "Exist", "Expect", "Explain",
    "Explore", "Express", "Fail", "Fall", "Feed", "Feel", "Fight", "Find", "Finish", "Fit",
    "Fix", "Fly", "Follow", "Forgive", "Freeze", "Get", "Give", "Go", "Grab", "Grow",
    "Guess", "Handle", "Hate", "Have", "Hear", "Help", "Hide", "Hit", "Hold", "Hope",
    "Hurry", "Imagine", "Improve", "Include", "Increase", "Influence", "Inform", "Injure", "Inspire", "Insist",
    "Different", "Difficult", "Diligent", "Dim", "Direct", "Dirty", "Distant", "Distinct", "Disturbing", "Dizzy",
    "Dry", "Eager", "Early", "Easy", "Elegant", "Embarrassed", "Empty", "Encouraging", "Energetic", "Enthusiastic",
    "Equal", "Essential", "Evil", "Exact", "Excited", "Expensive", "Expert", "Faint", "Fair", "Familiar",
    "Famous", "Fancy", "Fantastic", "Fast", "Fat", "Fearful", "Fearless", "Fertile", "Festive", "Few",
    "Fierce", "Filthy", "Fine", "Firm", "Flat", "Flawless", "Flexible", "Free", "Frequent", "Friendly",
    "Frightened", "Frightening", "Full", "Funny", "Furious", "Generous", "Gentle", "Genuine", "Giant", "Gifted",
    "Glad", "Gleaming", "Gloomy", "Glorious", "Good", "Graceful", "Grateful", "Great", "Greedy", "Green",
    "Guilty", "Handsome", "Happy", "Hard", "Harsh", "Healthy", "Heavy", "Helpful", "Helpless", "Hidden",
    "High", "Hilarious", "Honest", "Honorable", "Hopeful", "Horrible", "Hot", "Huge", "Humid", "Hungry"

]


