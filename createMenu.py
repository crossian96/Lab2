def createMenu(listOfChoices):
    """
    Description: returns a STRING of numbered menu options
    PreConditions: listOfChoices is a list of strings that indicate menu choices
    """
    l = listOfChoices
    s = "" + '\n\n' 
    for i in range(len(l)):
        s = s + str(i + 1) + ") " + l[i] + "\n"
    return s
