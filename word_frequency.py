STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

sen = 'seneca_falls.txt'
eman = 'emancipation_proclamation.txt'

def clean_string(string):
    """Remove whitespace and punctuation and converts to lowercase"""
    s = ''
    for char in string.lower():
        if char.isalpha() or char == '-':
            s+= char
    return s

def double_hyphen_case(line):
    split_line = line.split('--')
    new_line = ''
    for split in split_line:
        new_line += ' '+split
    return new_line

def print_word_freq(file):
    """Read in 'file' and print out the frequency of words in that file."""
    collector = {}
    just_width = 0
    with open(file, 'r') as text:
        lines = text.readlines()

    for line in lines:
        line = double_hyphen_case(line)
        for word in line.split(' '):
            word = clean_string(word)
            if len(word)>0 and word not in STOP_WORDS:
                if len(word) > just_width:
                        just_width = len(word)
                if word in collector:
                    collector[word] += '*'
                elif word not in collector:
                    collector[word] = '*'
    for word, count in collector.items():
        print(f'{word.rjust(just_width)} | {str(len(count)).ljust(2)} {count}')
    return collector

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
