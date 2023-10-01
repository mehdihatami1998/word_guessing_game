
def get_user_input():
    user_input = input("Guess which letter exists in the word: ")
    if len(user_input) == 1:
        return user_input
    elif len(user_input) == 0:
        print("You didn't type anything. Please type a letter.")
        validate_user_input()
    elif len(user_input) > 1:
        print("You typed more than one letter. Please type only one letter.")
        validate_user_input()


if __name__ == "__main__":

    validate_user_input()

