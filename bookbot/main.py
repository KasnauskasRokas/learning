path_to_file = 'books/frankenstein.txt'


def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_lines(file_contents)
        char_list = count_chars(file_contents)
    print_results(word_count, char_list)


def sort_on(dict):
    return dict["num"]


def count_lines(file_contents):
    return len(file_contents.split())


def convert_dict_to_list(char_dict):
    char_list = []
    for key, value in char_dict.items():
        char_list.append({'letter': key, 'num': value})
    return char_list


def count_chars(file_contents):
    char_dict = {}
    words = file_contents.split()
    for word in words:
        for char in word:
            if char.lower() in char_dict:
                char_dict[char.lower()] += 1
            else:
                char_dict[char.lower()] = 1
    list = convert_dict_to_list(char_dict)
    list.sort(key=sort_on, reverse=True)
    return list


def print_results(word_count, char_list):
    print(f'--- Begin report of {path_to_file} ---')
    print(f'{word_count} words found in the document')
    print('\n')
    for char in char_list:
        print(f"The '{char['letter']}' character was found {char['num']} times")
    print('--- End report ---')


main()
