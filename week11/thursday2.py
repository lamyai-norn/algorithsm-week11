def numberOfUpperCase(word):
    letterUpper=0
    for n in range(len(word)):
       letter=word[n]
       if letter.upper()==letter:
          letterUpper=letterUpper+1
    return letterUpper
word=input("Word : ")
print("Number of uppercase letters : ",numberOfUpperCase(word))
