def main ():
    # get book text
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    num_words = get_num_words(text)

    # remove non-alpha characters, transform all to lowercase
    cleaned_text = get_clean_text(text)

    # create sorted list of chars, most frequent to least
    char_dict = get_char_dict(cleaned_text)
    char_sorted_list = char_dict_to_sorted_list(char_dict)
            
   
    # create report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for d in char_sorted_list:
        print(f"The '{d['char']}' character was found {d['num']} times")
    print("--- End report ---")

# read in text from file path
def get_book_text(path):    
    with open(path) as f:
        return f.read()

# count how many words in text
def get_num_words(text):
    words = text.split()
    return len(words)

# removes non-alpha characters and makes all lowercase
def get_clean_text(text):
    cleaned_text = []
    for char in text:
        if char.isalpha():
            lowered = char.lower()
            cleaned_text.append(lowered)
    return cleaned_text

# create a dictionary of characters
def get_char_dict(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# transform from dict to sorted list of dicts
def char_dict_to_sorted_list(char_dict):
    dict_list = []
    for d in char_dict:
        dict_list.append({"char": d, "num": char_dict[d]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

# to enable sorting of dict values
def sort_on(dic):
    return dic["num"]

main()