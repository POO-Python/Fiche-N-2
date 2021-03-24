from math import *


def main() : 
    def roots(a, b, c):
        try:
            a = float(a)
            b = float(b)
            c = float(c)
            if a == 0:
                print("Calcul impossible : le premier paramètre ne doit pas être égal à zéro.")
            else:
                delta = b ** 2 - 4 * a * c
                if delta > .0:
                    x1 = (-b - sqrt(delta)) / (2 * a)

                    x2 = (-b + sqrt(delta)) / (2 * a)
                    print("Le polynôme a deux racines réelles distinctes :", x1, "et", x2)
                elif delta == .0:
                    x = -b / (2 * a)
                    print("Le polynôme a une racine réelle double :", x)
                else:
                    print("Le polynôme n'a pas de racine réelle.")
        except:
            print("Calcul impossible : les paramètres doivent être des nombres.")


    roots(1, 'b', 3)
    roots(0, 1, 2.5)
    roots(1, 1, 1)
    roots(1, 2, 1)
    roots(1, 5.2, 1.4)

main()
