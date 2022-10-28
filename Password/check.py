import random
from string import ascii_lowercase
class check:
    def guessLettre(mots):
        passwords = []
        mots = ["joachim"]
        password = ''
        
        while (password not in passwords):
            for mot in mots:
                mot.upper()
                mdp = random.choices([mot.join(random.choices(ascii_lowercase, k=3)) for _ in range(10)])
                if(mdp.isUpper()):
                    if(mdp not in mots):
                        mots.append(mdp)
                        password = mdp   
                        passwords.append(password)
                else:
                    if(mdp not in mots):
                        mots.append(mdp)
                        password = mdp   
                        passwords.append(password)
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
    # def gussDate(mots):
