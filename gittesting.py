greetings = "hello,hi,how do you do".split(',')

for greet in greetings:
    if greet != "how do you do":
        print(greet + ':)')
    else:
        print(greet)
