def getComment(grade):
    if grade > 10 :
        return "Good"
    return "Bad"
print(getComment(12)+getComment(8))