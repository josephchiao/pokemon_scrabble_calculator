def scrabble_calculator(word):
    
    word = word.lower()
    score = 0
    letter_score = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3,
                    'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

    for letter in range(len(word)):
        if word[letter] in letter_score:
            score += letter_score[word[letter]]

    return score
        
def data_interpreter():

    def_scores = {}
    data = open("pokemon_data_1.txt").read().splitlines()

    for pokemon in range(1010):
        name = data[pokemon*21+2].split('"')[0]
        def_scores[name] = int(data[pokemon*21+14])

    return def_scores

def scrabble_defense_score():
    def_scores = data_interpreter()
    for name in def_scores:
        def_scores[name] *= scrabble_calculator(name)

    return def_scores

main_list = sorted(scrabble_defense_score().items(), key=lambda x:x[1])
print("\n\n\n", main_list[-1])