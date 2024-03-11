import random  

Pocetbodu = 0

plusbody = 1

def PocetB (Pocetbodu, plusbody):
    PocetboduF = Pocetbodu + plusbody
    return PocetboduF
    
def nasobeni(a,b):
    vysledek = a * b
    return vysledek

def vyhodnoceni(vysledek, porovnani):
    odpoved = False
    if vysledek == porovnani:
        print("ty jsi ale šikulka, mas to spravne")
        odpoved = True
        PocetboduF = PocetB(Pocetbodu, plusbody)
        Pocetbodu = PocetboduF
        print ("Mate", PocetboduF, "bodu")
    else:
        print("achjoo")
    return odpoved
    
for x in range(9):

    a = random.randint(1,10)
    b = random.randint(1,10)

    porovnani = input(f"{a} * {b} = ")
    porovnani = int(porovnani)
    vysledek = nasobeni(a, b)
    vyhodnoceni(vysledek, porovnani)
else:
    print("konecne hotovo, jupiiii")

