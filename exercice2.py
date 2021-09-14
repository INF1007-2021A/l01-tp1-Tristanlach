import math


def resoudreEquation(a, b, c):
    # TODO: Calculer le discriminant et assigner la valeur dans la variable "delta"
    delta = (b**2) - (4*a*c)

    # TODO: Déterminer la condition (bool) qui correspond à aucune solution de l'équation et mettre la valeur dans la variable "naPasDeSolution"
    naPasDeSolution = delta < 0

    if naPasDeSolution:
        print("Aucune racine")
        # ne pas modifier
        return None

    # TODO: Déterminer la condition (bool) qui correspond à une unique solution de l'équation et mettre la valeur dans "aUneSeuleSolution"
    aUneSeuleSolution = delta == 0
    if aUneSeuleSolution:
        print("Une seule racine")
        # TODO: assigner a la variable x1 la valeur de la racine
        x1 = 0
        # ne pas modifier
        return x1

    # TODO: Déterminer la condition (bool) qui correspond à deux solutions de l'équation et mettre la valeur dans "aDeuxSolutions"
    aDeuxSolutions = delta > 0

    if aDeuxSolutions:
        # TODO: afficher sur l'écran "Deux racines"
        print("Deux racines")
        # TODO: calculer la premiere racine, assigner la a "x1"
        x1 = math.sqrt(delta)

        # TODO: calculer la deuxieme racine, assigner la a "x2"
        x2 = -(math.sqrt(delta))

        # ne pas modifier cette ligne
        return x1, x2


if __name__ == '__main__':
    a = int(input("Entrez a, non nul: "))
    b = int(input("Entrez b: "))
    c = int(input("Entrez c: "))

    print(resoudreEquation(a, b, c))
