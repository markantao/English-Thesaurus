import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean " + get_close_matches(w,
                                                       data.keys())[0] + " instead: Y/N: ")
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]

        elif yn == "N":
            return "Ok"

        while yn != "Y" or "N":
            yn = input("Did you mean " + get_close_matches(w,
                                                           data.keys())[0] + " instead: Y/N: ")
            if yn == "Y":
                return data[get_close_matches(w, data.keys())[0]]

    else:
        return "The word doesn't exist. Please try again."


word = input("Enter Word: ")

print(translate(word))
