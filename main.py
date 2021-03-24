from math import *


def main() : 
    def calcul(x):
        
        return sqrt(x) / (x - 2)

    try:
        saisie = float(input("Veuillez Saisir un nombre x: "))
        print(calcul(saisie))
    except ValueError: 
        print("Veuillez entrer un nombre positif.")
        main()
    except ZeroDivisionError:
        print("Vous avez saisie un nombre effectuant une division par 0.")
        main()
    except Exception:
        print("Une erreur c'est produite.")

main() 
