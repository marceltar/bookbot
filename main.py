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

def main ():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()

    cleaned_text = cleaning_text(file_contents)

    dic = make_dic(file_contents)
    
    
    word_count = word_counting (file_contents)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    print(char_count)
    print("--- End report ---")

main()