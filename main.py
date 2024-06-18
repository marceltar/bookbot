# removes non-alpha characters and makes all lowercase
def cleaning_text(text):
    cleaned_text = []
    for char in text:
        if char.isalpha():
            cleaned_text.append(char.lower())
    return cleaned_text

# count how many words in text
def word_counting(text):
    return(len(text.split()))

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

def main ():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()

    word_count = word_counting (file_contents)

    cleaned_text = cleaning_text(file_contents)

    dic = make_dic(cleaned_text)
    
    dic_list = []
    for d in dic:
        dic_list.append({"char": d, "num": dic[d]})
    
    dic_list.sort(reverse=True, key=sort_on)
   

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for d in dic_list:
        char = d["char"]
        num = d["num"]
        print(f"The \'{char}\' character was found {num} times")
    print("--- End report ---")

main()