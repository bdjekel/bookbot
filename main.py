def main():
    file_location = "books/frankenstein.txt"
    content_string = get_file_content(file_location)
    word_count = count_words(content_string)

    print(f"{word_count} words in document")

def get_file_content(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(file_contents):
    word_list = file_contents.split()
    return len(word_list)
    
main()