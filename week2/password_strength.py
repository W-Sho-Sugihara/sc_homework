LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r",encoding="utf-8") as file:
        content = file.read()
        if case_sensitive:
            return  word in content
        else: 
            return word.lower() in content.lower()
                
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
    elif word_in_file(password, "toppasswords.txt"):
        print("Password is a commonly used password and is not secure.")
        return 0
    elif len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    elif len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    else:
        return word_complexity(password) + 1

def main():
    password = ""
    while True:
        password = input("Please enter your password (Enter q/Q to exit): ")
        if password.lower() == "q":
            break
        print(f"Password strength is: {password_strength(password)}")
    
    print("Goodbye")


if __name__ == "__main__":
    main()
