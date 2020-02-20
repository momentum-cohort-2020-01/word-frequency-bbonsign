from functools import reduce

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with', ''
]

sen = 'seneca_falls.txt'
eman = 'emancipation_proclamation.txt'


def clean_string(string):
    """Remove whitespace and punctuation and converts to lowercase"""
    return ''.join(filter(lambda char: char.isalpha() or char == '-', string.lower()))


def double_hyphen_case(line):
    split_line = line.split('--')
    new_line = ''
    for split in split_line:
        new_line += ' '+split
    return new_line


def count_words(file):
    collector = {}
    with open(file, 'r') as text:
        lines = text.readlines()
    for line in lines:
        line = double_hyphen_case(line)
        for word in line.split(' '):
            word = clean_string(word)
            if word not in STOP_WORDS:
                collector[word] = collector.get(word, 0) + 1
    return collector


def get_just_width(dic):
    """returns max length of key in dic for pretty printing"""
    return reduce(lambda a, b: a if a > b else b, [len(key) for key in dic.keys()])


def make_stars(n):
    return '*'*n


def print_word_freq(file):
    """Read in 'file' and print out the frequency of words in that file."""
    counts = count_words(file)
    just_width = get_just_width(counts)
    for word, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{word.rjust(just_width)} | {str(count).ljust(2)} {make_stars(count)}")


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
