
import random
from tabnanny import check
import random
from string import ascii_lowercase, ascii_uppercase

from Password import PasswordClass
def guessLettre(mots):
        passwords = []
        mots = ["joachim"]
        password = ''
        
        while (password not in passwords):
            for mot in mots:
                mdp = random.choices([mot.join(random.choices(ascii_lowercase, k=len(mot))) for _ in range(10)])
                if(mdp not in mots):
                    mots.append(mdp)
                    password = mdp   
                    passwords.append(password)
            for mot in mots:
                mdp = random.choices([mot.join(random.choices(ascii_uppercase, k=len(mot))) for _ in range(10)])
                    
        return passwords   
def guessLeet(mots):
        passwords = []
        mots = ["joachim"]
        password = ''
        leet = {'a':'4','e':'3','i':'1','o':'0','A':'4','E':'3','I':'1','O':'0'}
        for mot in mots:
            for i in len(mot):
                for lettre in mot[i]:
                    for key in leet:
                        if(lettre == key):
                            count = mots[i].count(lettre)
                            for j in range(count):
                                mot.append(mot[i].replace(lettre, leet[key],j))
                            mot.append(mot[i].replace(lettre, leet[key]))
                            mot[i] = mot[i].replace(lettre, leet[key])
                                
            mot = list(dict.fromkeys(mot))
            passwords.append(mot)
        return passwords


mots = ["joachim","Dan"]

answer = guessLettre(mots)
answer2 = guessLeet(mots)

print(answer)