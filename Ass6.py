def WriteoutLines(TheDict,choice):
    num = 0
    list = TheDict.get(choice)
    while num != len(list):
        print(list[num])
        num += 1
        
#replace this with whatever you want
TheDict = {"pres":["the President right now is",
                        "Joe Biden"],
           "FSUNick":["the seminoles",
                      "unconquerd"],
           "class":["introcution to Python"]
           }
TheKeys = list(TheDict.keys()) #we need to convert TheDict.keys to a list
    
Done = False
while (not Done):
    print("we have these keys")
    for i in range(0, len(TheKeys)):
       print(TheKeys[i])
    print("enter zz to end program or the word you want a listing for")
    choice = input("enter the string you want typed out")


    if (choice in TheDict.keys()):
           WriteoutLines(TheDict,choice)
  
    elif (choice == "zz"):
        break
    else:
        print("The was not a legal choice")
