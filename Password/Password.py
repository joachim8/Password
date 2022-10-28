
from datetime import date
import random
from string import ascii_lowercase

class PasswordClass(object):
    """description of class"""
    #caractere_sp =  []
    mots = []
    age = date


    def __init__(self,mots,age):
        self.mots = mots
        #self.nom = nom
        #self.prenom = prenom
        self.age = age
        #self.caractere_sp = ['!','"','#''$','%&','(',')','*','+','-','.','/',':',';','<','=','>','?','@','[','\'',']','^','_','`','{','|','}']

    def mots(self) :
        return self.mots

    #def nom(self):
    #    return self.nom
    #def prenom(self) : 
    #    return self.prenom
    def age(self):
        return self.age

    def guessLettre(mots, password, mot):
        passwords = []
        mots = []
        password = ''
        lettres = mot[0:3]
        leet = {'a':'4','e':'3','i':'1','o':'0','A':'4','E':'3','I':'1','O':'0'}
        while (password not in passwords):
            for mot in mots:
                mdp = random.choices([lettres.join(random.choices(ascii_lowercase, k=3)) for _ in range(10)])
                mdp.upper()
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
            for mot in mots:
                mdp = random.choice()


        return passwords   


  
