from utils import word_generator
from utils import input_validator
from utils import hint_generator


def main():

    word_generator.generate_word()
    #print(f"selected word is {word_generator.word} from {word_generator.word} category")

    user_input = input_validator.get_user_input()
if __name__ == "__main__":
    main()