def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    cleaned_text = cleaning_text(text)

    dic = make_dic(cleaned_text)
    
    dic_list = []
    for d in dic:
        dic_list.append({"char": d, "num": dic[d]})
    
    dic_list.sort(reverse=True, key=sort_on)
   

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for d in dic_list:
        char = d["char"]
        num = d["num"]
        print(f"The \'{char}\' character was found {num} times")
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
def cleaning_text(text):
    cleaned_text = []
    for char in text:
        if char.isalpha():
            cleaned_text.append(char.lower())
    return cleaned_text



# create a dictionary of characters
def make_dic(text):
    char_count = {}
    for char in text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(dic):
    return dic["num"]

main()