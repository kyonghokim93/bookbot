# print("hello world")

def main():
    book_path = "books/frankenstein.txt"
    text = get_booktext(book_path)
    lower_text = uncapitalize(text)
    num_words = get_num_words(text)
    lower_dictionary = count_letters(lower_text)
    list_of_dict = convert_to_list(lower_dictionary)
    alpha_dict = remove_nonalpha(list_of_dict)
    alpha_dict.sort(reverse=True, key=sort_on)
    print_report(book_path,num_words,alpha_dict)

def print_report(path,num,list_of_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{num} words found in the document")
    print()
    for onedict in list_of_dict:
        print(f"The '{onedict["letter"]}' character was found {onedict["count"]} times")
    print("--- End report ---")

def remove_nonalpha(list_of_dict):
    #for onedict in list_of_dict[:]:
    #    if not onedict["letter"].isalpha():
    #        list_of_dict.remove(onedict)
    list_of_dict = [x for x in list_of_dict if x["letter"].isalpha()]

    return list_of_dict

def get_booktext(path):
    with open(path) as f:
        return f.read()

def uncapitalize(text):
    lower = text.lower()
    return lower

def count_letters(lower_text):
    lower_dictionary = {}
    for letter in lower_text:
        if letter not in lower_dictionary:
            lower_dictionary[letter] = 1
        else:
            lower_dictionary[letter] += 1
    return lower_dictionary

def convert_to_list(dictionary):
    templist = []
    for x, y in dictionary.items():
        tempdict = {}
        tempdict.update({"letter": x})
        tempdict.update({"count": y})
        templist.append(tempdict)
    return templist

def sort_on(dict):
    return dict["count"]

def get_num_words(text):
    words = text.split()
    return len(words)


main()
