
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = secondes / 31536000

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    annees_restantes = annees - int(annees)
    semaines = annees_restantes * 52

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    semaines_restantes = semaines - int(semaines)
    jours = semaines_restantes * 7

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    jours_restants = jours - int(jours)
    heures = jours_restants * 24

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    heures_restantes = heures - int(heures)
    minutes = heures_restantes * 60

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    minutes_restantes = minutes - int(minutes)
    secondes = minutes_restantes * 60


    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(annees ,semaines ,jours ,heures ,minutes ,secondes)

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
