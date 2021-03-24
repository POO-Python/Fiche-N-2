from math import *


def main() : 
    def calcul(x):
        
        return sqrt(x) / (x - 2)

    try:
        saisie = float(input("Saisir un nombre x: "))
        print(calcul(saisie))
    except ValueError: 
        print("Veuillez entrer un nombre positif.")
        main()
    except ZeroDivisionError:
        print("Vous avez saisie un nombre effectuant une division par 0.")
        print("Veuillez recommencer.")
        main()
    except Exception:
        print("Une erreur c'est produite.")

main()