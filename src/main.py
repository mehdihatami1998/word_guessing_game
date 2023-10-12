from utils import word_generator
from utils import input_validator
from utils import hint_generator


def main():

    selected_word = word_generator.generate_word()
    print(selected_word)
    print(f"you need to guess the right letters instead of underscores")

    blank_word = "_ " * len(selected_word)   
    print(f"{blank_word}")

    number_of_guesses = len(selected_word)
    print(f"you can have {number_of_guesses} wrong guesses")
    wrong_guesses =""

    while True:
        
        user_input = input_validator.get_user_input()
        index = []
    
        if user_input in selected_word:
            for i in range(len(selected_word)):
                if user_input == selected_word[i]:
                    index.append(i)
            

            for j in range(len(index)):
                real_index = index[j]
                blank_word = blank_word[:real_index*2] + user_input + blank_word[real_index*2 + 1:]
            print(f"Good guess!, the letter {user_input} appears {len(index)} times in the word")
            print(blank_word)
            print(wrong_guesses)
            #print(blank_word)

        else:
            number_of_guesses = number_of_guesses - 1
            wrong_guesses = wrong_guesses + user_input + " "
            print(f"Sorry!, the letter {user_input} does not exists in the word")
            print(f"you can still have {number_of_guesses} wrong guesses")
            
            print(blank_word)
            print(wrong_guesses)
            
            

            if len(wrong_guesses.replace(" ", "")) >= len(selected_word):
                print("Sorry!, you have guessed too many wrong letters. The word was " + selected_word)
                break

            print("Do you need a hint? (y/n)")
            need_hint = input("Do you need a hint? (y/n)")
            if need_hint == "y":
                hint_generator()

        
        if blank_word.replace(" ", "") == selected_word:
            print("Congratulations!, You guessed the word!")
            break
    #print(blank_word)
    ask_if_again = input("Do you wanna play again? (y/n)")
    if ask_if_again == "y":
        main()
    else:
        print("Thanks for playing word guesser game")
        print("Hope to see you again!")
if __name__ == "__main__":
    main()