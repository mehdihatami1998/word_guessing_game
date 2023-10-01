import random

word_categories = {
    "countries": ["brazil", "peru", "argentina", "chile", "colombia", "uruguay", "paraguay", "bolivia", "venezuela", "ecuador", "guyana", "suriname", ],
    "fruits": ["apples", "bananas", "oranges", "grapes", "strawberries", "watermelons", "pineapples", "mangos", "peaches", "pears", "cherries", "blueberries", "raspberries", "blackberries", "lemons", "limes", "coconuts", "avocados", "pomegranates", "kiwis", "papayas", "figs", "dates", "guavas", "lychees", "passion fruits", "persimmons", "plums", "pomegranates", "pomelos", "tangerines", "cantaloupes", "honeydew melons", "dragon fruits", "star fruits", "carambolas", "jackfruits", "durians", "breadfruits", "lychees", "mangosteens", "rambutans", "sapodillas", "sapotes", "tamarinds", "uglis", "yuzu"],
    "animals": ["elephant", "tiger", "giraffe", "lion", "zebra", "panda", "kangaroo", "koala", "cheetah", "gorilla", "hippopotamus", "rhinoceros", "chimpanzee", "leopard", "crocodile", "dolphin", "eagle", "flamingo", "jellyfish", "kangaroo", "parrot", "octopus", "penguin"],
    "colors": ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "white", "gray", "grey"],
    "sports": ["soccer", "basketball", "football", "baseball", "tennis", "volleyball", "golf", "hockey", "rugby", "cricket", "badminton", "bowling", "boxing", "cycling", "fencing", "gymnastics", "judo", "karate", "skiing", "snowboarding", "swimming", "taekwondo","wrestling"],
    "jobs": ["doctor", "nurse", "teacher", "engineer", "lawyer", "scientist", "programmer", "developer", "designer", "artist", "musician", "actor", "actress", "singer", "dancer", "chef", "cook", "firefighter", "soldier", "pilot", "mechanic", "electrician", "plumber", "carpenter", "farmer", "veterinarian", "dentist", "architect", "psychologist", "accountant", "economist", "writer", "journalist", "photographer", "librarian", "cashier", "secretary", "receptionist", "waiter"
    ]
}

def generate_word():
    category = random.choice(list(word_categories.keys()))
    word = random.choice(word_categories[category])
    printed = print( f"a word from the category of {category} is selected for you to guess")
    return word

if __name__ == "__main__":
    generate_word()