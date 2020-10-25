
def removeMinuses(word):
  newWord = ""
  for i in range(len(word)):
    char = word[i]
    if char !="-":
      newWord += char
  return newWord
condition=True
while condition:
  inputString=input("Enter a word:")
  print(removeMinuses(inputString))
  yesOrNo=input("Do you want to continue(Y/N)?:")
  if yesOrNo=="y" or yesOrNo=="Y":
    condition=True
  elif yesOrNo=="n" or yesOrNo=="N":
    condition=False
   
