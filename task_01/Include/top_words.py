from Include.file import File

class TopWords(File):
    def __init__(self, file: str):
        super().__init__(file)

    def top_words(self, top: int, reverse: bool = True):
        buffer: dict = self.words_counter()
        return sorted([(value, key) for key, value in buffer.items()], reverse=reverse)[:top]