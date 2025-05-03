# obtain a list of files in the input directory
import sys

from homework.src._internals.write_word_counts import write_count_words
from homework.src._internals.read_all_lines import read_all_lines


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # count the frequency of the words in the files in the input directory
    counter = read_all_lines()
    write_count_words(counter)


if __name__ == "__main__":
    main()
