def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    wc = text.split()
    return len(wc)

def sort_on(dict):
    return dict["count"]

def count_letters(text):
    lower_text = text.lower()
    letter_dict = {}
    for letter in lower_text:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1.

    letter_list = []
    for i in letter_dict:
        char_dict = {}
        char_dict["letter"] = i
        char_dict["count"] = letter_dict[i]
        letter_list.append(char_dict)
    
    letter_list.sort(reverse=True, key=sort_on)
    
    for i in range(len(letter_list)):
        extract = letter_list[i]
        print(f"{extract['letter']}: {int(extract['count'])}")