from random import randrange



def select_a_word(words_list):
    num = len(words_list)
    rand = randrange(0,num)
    print(rand)
    return words_list[rand]



