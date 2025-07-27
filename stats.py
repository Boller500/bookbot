def countwords(text):
    return len(text.split())

def countCharacters(text):
    text_lower = text.lower()
    char_list = list(text_lower)
    char_count_dict = {}
    for character in char_list:
        if character not in char_count_dict:
            char_count_dict[character] = 1
        else:
           char_count_dict[character] += 1
    return char_count_dict

def sort_dict(char_dict):
    sorting_dict = []
    def sort_on(items):
        return items["num"]
    
    for i in char_dict:
        sorting_dict.append({"char":i,"num": char_dict[i]})
    
    sorting_dict.sort(reverse=True, key=sort_on)
    return sorting_dict