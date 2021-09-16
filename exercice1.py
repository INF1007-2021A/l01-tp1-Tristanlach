def fizzBuzz(n):
    reponse = ""
    if n %3 == 0 and n %5 == 0 :
        reponse = "fizzBuzz"
    elif n %5 == 0 :
        reponse = "buzz"
    elif n %3 == 0 :
        reponse = "fizz"

    else:
        resultat = n

    resultat = reponse
    return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
