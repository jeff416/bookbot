def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document.")
    print()
    print(f"{letter_count}")
   
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
                letter_dict[letter] = 1

    #converting key and value into a list NEED TO make sepperate keys for letter and count eg "{'letter': 'a', 'count': 5}"
    #so I can use the sort_on function in the exmaple.
    
    letter_list = []
    for i in letter_dict:
        char_dict = {}
        #print(i)
        char_dict[i] = "count", letter_dict[i]
        print(letter_dict[i])
        letter_list.append(char_dict)
    
    #sort list and return
    #letter_list.sort(reverse=True, key=sort_on)
    return letter_list

main()