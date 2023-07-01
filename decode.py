import re
import nicknames


def get_mail_text():
    with open("mail.txt") as f:
        s = f.read()
    return s


if __name__ == "__main__": 
    decoded_sequence = {}
    mail_text = get_mail_text()

    our_names = nicknames.our_names()

    for our_name in our_names:
        for m in re.finditer(our_name.name, mail_text):
            decoded_sequence[m.span()[0]] = our_name.code
    
    sorted_sequence = sorted(decoded_sequence.items())

    for data in sorted_sequence:
        print(format(data[1], '#02X'), ":", chr(data[1]))
