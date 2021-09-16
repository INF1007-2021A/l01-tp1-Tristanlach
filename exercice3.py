
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = (secondes // (3600*24*365))
    secondes_restantes_01 = secondes - (annees * (3600*24*365))

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = secondes_restantes_01 // (3600*24*7)
    secondes_restantes_02 = secondes_restantes_01 - (semaines * (3600*24*7))

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = secondes_restantes_02 // (3600*24)
    secondes_restantes_03 = secondes_restantes_02 - (jours * (3600*24))

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = secondes_restantes_03 // (3600)
    secondes_restantes_04 = secondes_restantes_03 - (heures * 3600)

    # TODO: Assigner à la variable "minutes" le nombre de minutes restantes
    minutes = secondes_restantes_04 // (60)
    secondes_restantes_05 = secondes_restantes_04 - (minutes * 60)

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = secondes_restantes_05


    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
