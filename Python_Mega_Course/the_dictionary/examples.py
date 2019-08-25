import json
from difflib import SequenceMatcher, get_close_matches

# Reference (Python Standard Libraries): https://docs.python.org/3/library/index.html
data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist. Please double check it."


def matching_ratio(word1, word2):
    return SequenceMatcher(None, word1, word2).ratio()


def test_get_close_matches(word, list):
    return get_close_matches(word, list, n=2, cutoff=0.8)  # 2 means how many matches you would like to return
    # higher cutoff value checks more strictly


def main():
    # word = input("Enter word: ")
    # print(matching_ratio("rain", "rainn"))
    print(test_get_close_matches("rainn", ["rain", "chain", "gain", "pyramid"]))


if __name__ == '__main__':
    main()
