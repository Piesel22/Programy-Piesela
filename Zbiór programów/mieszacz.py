from random import randint

def run():
    zdanie = input("Podaj zdanie: ")
    zdanie.split()
    for litera in zdanie:
      los = randint(0, 2)
      zdanie = zdanie[1:] + zdanie[0]
      print(zdanie)
    input()