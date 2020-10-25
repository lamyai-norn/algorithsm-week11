def reverseString(word):
    result=""
    lastIndex=len(text1)-1
    for n in range(len(word)):
        result=result + text1[lastIndex-n]
    return result
text1=input("Text1 : ")
print(reverseString(text1))
