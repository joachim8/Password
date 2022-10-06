
import random

from Password import PasswordClass

def pasword_gen():
    passwords = []
    mots = []
    age = '22/05/1999'
    mot = 'Joachim'
    password = ''
    lettres = mot[0:3]
    while (password not in passwords):
      for mot in mots:
        mdp= random(lettres)
        mdp.upper()
        if(mdp not in mots):
         mots.append(mdp)
         password = password + mdp   
         passwords.append(password)
    return passwords   
  
 
answer = pasword_gen()

print(answer)




