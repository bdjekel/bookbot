def main():
    file_location = "books/frankenstein.txt"
    content_string = get_file_content(file_location)
    word_count = count_words(content_string)
    char_count = count_characters(content_string)
    print(f"{word_count} words in document")
    print(f"{char_count}")


def get_file_content(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(file_contents):
    word_list = file_contents.split()
    return len(word_list)

def count_characters(file_contents):
    char_counts = {}
    lowered_contents = file_contents.lower()
    for i in lowered_contents:
        if i in list(char_counts.keys()):
            char_counts[i] += 1
        else:
            char_counts[i] = 1
    return char_counts
    
main()