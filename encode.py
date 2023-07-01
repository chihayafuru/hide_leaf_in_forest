import re
import nicknames

def base_text():
    with open("cover_message.txt") as f:
        s = f.read()
    return s


def split_text(text):
    return re.split(r'私たち', text)


def get_secret_code_sequence():
    message = "Nagano Hackathon"
    b = bytes(message, 'utf-8')
    return b


if __name__ == "__main__": 
    base_text = base_text()
    splited_text = split_text(base_text)
    you_and_i = nicknames.our_names()

    sentence_count = len(splited_text)

    merged_array = []

    secrets = get_secret_code_sequence()

    for counter in range(sentence_count):
        if counter > 0:
            merged_array.append(you_and_i[secrets[counter-1]].name)
        merged_array.append(splited_text[counter])

    result_text = ''.join(merged_array)

    print(result_text)

