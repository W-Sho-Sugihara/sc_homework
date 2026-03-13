# added a message notifying users who enter short passwords how many more characters they need to make a strong password.
# added a missing char type message and function to determine missing types

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r",encoding="utf-8") as file:
        for line in file:
            file_word = line.strip()
            if case_sensitive:
                if word == file_word:
                    return True
            else:
                if word.lower() == file_word.lower():
                    return True
    return False
                
def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    result = 0
    if word_has_character(word, LOWER):
        result += 1
    if word_has_character(word, UPPER):
        result += 1
    if word_has_character(word, DIGITS):
        result += 1
    if word_has_character(word, SPECIAL):
        result += 1
    return result

def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt"):
        print("Password is a dictionary word and is not secure.")
        return 0
    elif word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    elif len(password) < min_length:
        print(f"Password is too short and is not secure. Enter password with more than 15 characters for a strong password. Add {strong_length - len(password)} more characters for a strong password.")
        return 1
    elif len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    else:
        return word_complexity(password) + 1
    
def get_missing_types(password):
    missing = []
    if not word_has_character(password, LOWER):
        missing.append("Lowercase")
    if not word_has_character(password, UPPER):
        missing.append("Uppercase")
    if not word_has_character(password, DIGITS):
        missing.append("Digits")
    if not word_has_character(password, SPECIAL):
        missing.append("Special Characters")
    return missing

def main():
    password = ""
    while True:
        password = input("Please enter your password (Enter q/Q to exit): ")
        if password.lower() == "q":
            break

        strength = password_strength(password)
        missing = get_missing_types(password)

        if missing:
            print(f"Password strength is: {strength}/5. Missing: {', '.join(missing)}")
        else:
            print(f"Password strength is: {strength}/5.")
    
    print("Goodbye")


if __name__ == "__main__":
    main()
