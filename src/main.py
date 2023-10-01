from utils import word_generator
from utils import input_validator
from utils import hint_generator


def main():

    selected_word = word_generator.generate_word()
    print(selected_word)
    print(f"you need to guess the right letters instead of underscores")
    blank_word = "_ " * len(selected_word)   
    print(f"{blank_word}")


    while True:
        
        user_input = input_validator.get_user_input()
        index = []
        for i in range(len(selected_word)):
            if user_input == selected_word[i]:
                index.append(i)
        for j in range(len(index)):
            real_index = index[j]
            blank_word = blank_word[:real_index*2] + user_input + blank_word[real_index*2 + 1:]
        print(blank_word)
        if blank_word.replace(" ", "") == selected_word:
            print("Congratulations!, You guessed the word!")
            break

if __name__ == "__main__":
    main()