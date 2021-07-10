from translate import Translator

tran = Translator(to_lang='no')
greetings = "hello,hi,how do you do".split(',')

for greet in greetings:
    if greet != "how do you do":
        print(tran.translate(greet) + ':)')
    else:
        print(tran.translate(greet))
