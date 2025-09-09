def count_words(contents):
    words = contents.split()
    print (f"Found {len(words)} total words")

def count_characters(contents):
    alphabet = {
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0
    }
    for char in contents:
        for letter in alphabet:
            if letter == char.lower():
                alphabet[letter] +=1
    
    return alphabet

def sort_on(items):
    return items["num"]

def sort_dict (count_dict):
    dict_list=[]
    for char,num in count_dict.items():
        dict_list.append({"char":char,"num":num})

    dict_list.sort(reverse=True,key=sort_on)

    for item in dict_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
