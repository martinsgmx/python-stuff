class File:
    def __init__(self, file: str):
        self.file: str = file
        self.buffer = list

    def name_file(self):
        return self.file

    def open_file(self):
        try:
            self.buffer = open(self.file, mode="r", encoding="utf-8").read().lower().split()
        except FileNotFoundError:
            print("Please verify your file!")
            exit()

    def words_counter(self):
        words: dict = {}

        for key in self.buffer:
            words[key] = words.get(key, 0) + 1

        return words