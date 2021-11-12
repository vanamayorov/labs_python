# Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
# Determine the required attributes-data and attributes-methods in class for working with the text file.
import re
import os

"""Script with FileParser class which performs statistical processing of a text file"""


class FileParser:
    """FileParser class with count words, count chars, count sentences, and get words dictionary methods"""

    def __init__(self, path):
        self.path = path

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError

        self.__path = path

    def count_words(self):
        """Count words

        Goes through lines in the file, counts words, and returns words number
        """
        words_num = 0
        with open(self.path, encoding='utf-8') as f:
            for line in f:
                word_list = re.findall(r'[\'\-\w]+', line)
                # \w matches a word character [a-zA-Z0-9_]

                words_num += len(word_list)

        return words_num

    def count_chars(self):
        """Count chars

        Goes through lines in the file, counts chars, and returns chars number
        """
        chars_num = 0
        with open(self.path, encoding='utf-8') as f:
            for line in f:
                chars_num += len(line)

        return chars_num

    def count_sentences(self):
        """Count sentences

        Goes through lines in the file, counts sentences, and returns sentences number
        """
        sentences_num = 0
        with open(self.path, encoding='utf-8') as f:
            for line in f:
                sentences_num += len(list(filter(None, re.split(r'\b[\.?!][A-Z\s+]', line))))
                # filter(None) is a shorthand for filter(lambda x: x)

        return sentences_num

    def get_words_dict(self):
        """Get each word and number of how many times it appears in the file

        Goes through lines in the file, adds words to the dictionary, and then checks if word already exists in the
        dictionary. If so, increases number of this word, otherwise adds the word to the dictionary.
        Then loops through dictionary and returns a string with words info.
        """
        output = ''
        word_counter = {}
        with open(self.path, encoding='utf-8') as f:
            for line in f:
                word_list = line.replace(',', '').replace('.', '').lower().split()
                for word in word_list:
                    if word not in word_counter:
                        word_counter[word] = 1
                    else:
                        word_counter[word] += 1

        for (word, occurrence) in word_counter.items():
            output += f'{word} - {occurrence}\n'
        return output


def main():
    try:
        file_name = 'readme.txt'
        output_file_name = 'file_info.txt'
        read_file = FileParser(file_name)
        info = f'readme.txt Info:\nNum of words: {read_file.count_words()}\nNum of chars: {read_file.count_chars()}\n' \
               f'Num of sentences: {read_file.count_sentences()}\nNum of each word:\n{read_file.get_words_dict().strip()}'
        with open(output_file_name, 'w') as f:
            print(info, file=f)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
