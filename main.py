import sys
from stats import count_words, count_char, report
def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 2:
        fpath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #fpath = "books/frankenstein.txt"
    txt = get_book_text(fpath)
    w_cnt = count_words(txt)
    c_count = count_char(txt)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fpath}...")
    print("----------- Word Count ----------")
    print(f"Found {w_cnt} total words")
    print("--------- Character Count -------")
    
    report(c_count)

main()

