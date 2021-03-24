from math import sqrt

def calcul(x):
    if x < 0 :
        raise ArithmeticError()

    if x == 2.0 :
        raise ZeroDivisionError()
        
    return sqrt(x) / (x - 2)

def main() : 
    print("Pour quitter le programme, entrer exit")
    saisie = input("Sinon, veuillez saisir un nombre x: ")
    if saisie == "exit":
        exit(0)
    else:
        try:
            print(calcul(float(saisie)))
        except ValueError: 
            print("Veuillez entrer un nombre.")
            main()
        except ZeroDivisionError:
            print("Vous avez saisie un nombre effectuant une division par 0.")
            main()
        except ArithmeticError:
            print("Veuillez entrer un nombre positif.")
            main()
        except Exception:
            print("Une erreur c'est produite.")
            main()

main()
