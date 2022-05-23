def who_are_you():
    users = ("Damian", "Gaba")
    newcomer = input("Kim jesteś? \n")
    useregzist = False

    for item in users:
        while useregzist == False:
            if item == newcomer:
              print("Poprawnie")
              useregzist = True
            else:
               newcomer = input("Zle! Kim jests \n")


