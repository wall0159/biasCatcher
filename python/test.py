import spacy
nlp = spacy.load("en_core_web_lg")

text = 'his ambition was to be the best of them all'

wordsToRemove = list()

problemWords = 'he she his her'
problemWordsNLP =  nlp(problemWords)
problemWordsList = problemWords.split(" ")

listWords = text.split(" ")
listNums = [0] * len(listWords)
for i in range(0,len(listWords)):
    # identify the problem words here, return a list of words and a
    # list of bools that indicate which words are a problem
    thisTok = nlp(listWords[i])
    sim = thisTok.similarity(problemWordsNLP)
    print(sim)
    # print(listWords[i], probWord, sim)
    if sim > 0.65:
        listNums[i] = 1
        listWords[i] = listWords[i].upper()
        # print(listWords)
        break
print( " ".join(listWords) )
