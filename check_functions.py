from tokenize import Triple


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

def currency_checker(a):
  while True:
    if a == "PLN" or a == "USD":
      print('{a} jest ok')
      return(a)
      break
    else:
      print("Wprowadzono bledna wartosc\n")
      print("Akceptuje tylko USD i PLN")
      a = input("Podaj Walute PLN/USD")


