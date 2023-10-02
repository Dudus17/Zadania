print ("Hello")
symbol = input ("Jakie zadanie matematyczne chcesz wykonać? Dozwolone znaki to:\n +\n -\n *\n / \n\n").strip()
if symbol != "/" and symbol != "*" and symbol != "-" and symbol != "+":
    print("Symbol {} jest niedozwolony, dozwolone znaki to: +, -, *, /".format(symbol))
else:
    zmienna = int(input ("Podaj zmienną A: "))
    zmiennaB = float(input ("Podaj zmienną B: "))

    if symbol == "*":
        result = (zmienna * zmiennaB)
        print("Wynik:", result)
    elif symbol == "+":
        result = (zmienna + zmiennaB)
        print("Wynik:", result)
    elif symbol == "-":
        result = (zmienna - zmiennaB)
        print("Wynik:", result)
    elif symbol == "/":
        if zmiennaB == 0:
            print("Pamiętaj cholero nie dziel przez zero! :)")
        else:
            result = (zmienna / zmiennaB)
            print("Wynik:", result)