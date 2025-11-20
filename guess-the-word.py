import random

word_bank = [
    'boba', 'pizza', 'sushi', 'burger', 'pasta', 'salad', 'taco', 'ramen',
    'steak', 'curry', 'dumpling', 'sandwich', 'noodle', 'omelette', 'coffee',
    'smoothie', 'waffle', 'pancake', 'fries', 'nachos', 'scone', 'bagel', 
    'muffin', 'python', 'java', 'ruby', 'swift', 'javascript', 'html', 'css',
    'react', 'angular', 'django', 'flask', 'node', 'linux', 'android', 
    'typescript', 'roses', 'tulips', 'daisies', 'sunflower', 'orchid', 'lily',
    'cactus', 'bonsai', 'fern', 'ivy', 'maple', 'oak', 'pine', 'birch', 
    'willow', 'eagle', 'sparrow', 'parrot', 'penguin', 'dolphin', 'shark', 
    'whale', 'tiger', 'lion', 'zebra', 'giraffe', 'elephant', 'kangaroo', 
    'koala', 'panda', 'crocodile', 'alligator', 'butterfly', 'dragonfly', 
    'ladybug', 'spider', 'ant', 'beetle', 'grasshopper', 'cricket', 'snail',
    'worm', 'coral', 'jellyfish', 'seahorse', 'starfish', 'clam', 'oyster', 
    'lobster', 'crab', 'shrimp', 'squid', 'octopus', 'peach', 'mango', 'banana',
    'apple', 'grape', 'orange', 'kiwi', 'papaya', 'plum', 'cherry', 'berry', 
    'melon', 'coconut', 'fig', 'date', 'nectarine', 'apricot', 'persimmon',
    'quince', 'pomegranate', 'tangerine', 'clementine', 'lime', 'lemon',
    'avocado', 'broccoli', 'carrot', 'spinach', 'kale', 'lettuce', 'cabbage',
    'cauliflower', 'zucchini', 'cucumber', 'pepper', 'onion', 'garlic', 
    'potato', 'tomato', 'eggplant', 'squash', 'pumpkin', 'car', 'bike', 'train',
    'plane', 'boat', 'subway', 'bus', 'truck', 'scooter', 'skateboard', 
    'helicopter', 'yacht', 'zeppelin', 'spaceship', 'rocket', 'satellite', 
    'drone', 'hovercraft', 'tram', 'ferry', 'canoe', 'kayak', 'glider', 
    'zeppelin', 'monorail', 'trolley', 'ocean', 'river', 'mountain', 'forest',
    'desert', 'island', 'valley', 'canyon', 'waterfall', 'glacier', 'volcano',
    'lagoon', 'reef', 'savanna', 'jungle', 'swamp', 'marsh', 'prairie', 'tundra'
]

word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))

    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Great guess!")