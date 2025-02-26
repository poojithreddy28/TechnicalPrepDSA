def reverse_sentence(sentence):
    rev = ''
    list = sentence.split()
    for i in list:
        rev = i + ' ' +  rev
    print(rev)
sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)