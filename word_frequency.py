STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def clean_string(string):
    """Remove whitespace and punctuation and converts to lowercase"""
    s = ''
    for char in string.lower():
        if char.isalpha():
            s+= char
    return s

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    collector = {}
    just_width = 0
    with open(file, 'r') as text:
        lines = text.readlines()
        for line in lines:
            for word in line.split(' '):
                word = clean_string(word)
                if word not in STOP_WORDS and word in collector:
                    collector[word] += '*'
                    if len(word) > just_width:
                        just_width = len(word)
                elif word not in STOP_WORDS and word not in collector:
                    collector[word] = '*'
                    if len(word) > just_width:
                        just_width = len(word)
    for i,j in collector.items():
        print(f'{i.rjust(just_width)} | {len(j)} {j}')
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
