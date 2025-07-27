import sys

from stats import countwords
from stats import countCharacters
from stats import sort_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path =  sys.argv[1]
    book_text = get_book_text(book_path)
    book_words_count= countwords(book_text)
    resultdict= sort_dict(countCharacters(book_text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_words_count} total words")
    print("--------- Character Count -------")

    for i in resultdict:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

if __name__ == '__main__':
    main()