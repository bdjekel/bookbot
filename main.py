def main():
    file_location = "books/frankenstein.txt"
    content_string = get_file_content(file_location)
    word_count = count_words(content_string)
    char_count = count_characters(content_string)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words in document\n")
    sorted_char_count = generate_report(char_count)
    for i in sorted_char_count:
        char = i["character"]
        count = i["count"]
        print(f" The '{char}' character was found {count} times")
    print("--- End report ---")

def generate_report(character_count):
    def sort_on(character_count):
        return character_count["count"]
    
    sorted_character_counts = []
    for key, value in character_count.items():
        if key.isalpha():
            sorted_character_counts.append({"character": key, "count" : value})
        else:
            pass
    
    sorted_character_counts.sort(reverse=True, key=sort_on)
    return sorted_character_counts

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