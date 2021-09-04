import os.path
from Include.top_words import TopWords

def main():
    file: str = input("Please provide an file: ")

    if not os.path.exists(file):
        print("Something is wrong, are you sure that file exists?")
        exit()

    text: TopWords = TopWords(file=file)
    text.open_file()
    print(f"File selected: { text.name_file() }")

    top: int
    try:
        top = int(input("How many top words you need it (Default: 10)? "))
    except:
        top = 10

    print(f"\t== TOP {top} WORDS ==")
    print("\tTimes | Word")
    print("\t------------------")
    for word in text.top_words(top=top):
        print(f"\t{word[0]}:\t{word[1]}")


if __name__ == "__main__":
    main()

# la redécouverte