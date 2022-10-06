
from datetime import date

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



  
