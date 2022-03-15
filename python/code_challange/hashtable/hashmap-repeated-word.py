
def repeated_word(sentence):
    word = sentence.split(" ")


    array1= []

    for ch in word:
        if ch in array1:
            count +=1
            return ch
        else:
            array1.append(ch.lower())


print(repeated_word("Once upon summer time, there was summer brave princess who."))


