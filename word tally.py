sentence = input("Enter a sentence: ").lower()

def word_tally():
    from collections import Counter #Parang import random pero iba yung collection niya 
    words = sentence.split(' ')
    count = len(words) #Ito yung mismong words na mag priprint
    frequencies = Counter(words) #Counts the words
    print(f"{count} : {frequencies}")

print(word_tally())




    
        

