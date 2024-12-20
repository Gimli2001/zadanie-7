class MyText:
    def __init__(self, text):
        # Initialize the class with the given text
        self.text = text

    def word_count(self):
        """
        Returns the number of words in the text.
        Splits the text by whitespace to identify individual words
        and counts the number of elements in the resulting list.
        """
        words = self.text.split()
        return len(words)

    def words_longest_to_shortest(self):
        """
        Returns an ordered array of words, from longest to shortest.
        Splits the text into words, then sorts them by their length
        in descending order using the sorted() function.
        """
        words = self.text.split()
        return sorted(words, key=len, reverse=True)

    def words_alphabetical(self):
        """
        Returns an alphabetically ordered array of words.
        Splits the text into words, then sorts them alphabetically,
        ignoring case sensitivity by converting each word to lowercase.
        """
        words = self.text.split()
        return sorted(words, key=lambda word: word.lower())
if __name__ == "__main__":
    # Input text
    text = "An apple a day keeps the doctor away"

    # Create an instance of MyText with the provided text
    my_text = MyText(text)

    # Print the number of words in the text
    print("Number of words:", my_text.word_count())

    # Print the words ordered from longest to shortest
    print("Words from longest to shortest:", my_text.words_longest_to_shortest())

    # Print the words in alphabetical order
    print("Words in alphabetical order:", my_text.words_alphabetical())