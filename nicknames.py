class CodeName:
    def __init__(self, code, name):
        self.code = code
        self.name = name

def our_names():
    code = 0
    your_names = ['あなた', 'パパ', 'お父さん', 'おとうさん', 'まさくん', 'マサクン', 'まさクン', 'マサくん', 'まささん', 'マササン', 'まさサン', 'マサさん']
    my_names   = ['わたし', 'ワタシ', 'あたし', '私', '結衣', 'ゆいぴょん', 'ユイピョン', 'ゆいピョン', 'ユイぴょん', 'ゆいぽん', 'ユイポン']
    our_names  = []

    for your_name in your_names:
        for my_name in my_names:
            our_name = your_name + 'と' + my_name
            code_name = CodeName(code, our_name)
            our_names.append(code_name)
            code += 1
    return our_names


if __name__ == "__main__":
    for our_name in our_names(): 
        print('0x' + format(our_name.code, '02x'), our_name.name)
