print ("Hello")
symbol = input ("Jakie zadanie matematyczne chcesz wykonać? Dozwolone znaki to:\n +\n -\n *\n / \n\n")
if symbol != "/" and symbol != "*" and symbol != "-" and symbol != "+":
    print("Symbol",symbol,"jest niedozwolony, dozwolone znaki to: +, -, *, /")
else:
    zmienna = int(input ("Podaj zmienną A: "))
    zmiennaB = float(input ("Podaj zmienną B: "))

    if symbol == "*":
        result1 = (zmienna * zmiennaB)
        print("Wynik:", result1)
    if symbol == "+":
        result3 = (zmienna + zmiennaB)
        print("Wynik:", result3)
    if symbol == "-":
        result4 = (zmienna - zmiennaB)
        print("Wynik:", result4)
    if symbol == "/" and zmiennaB == 0:
            print("Pamiętaj cholero nie dziel przez zero! :)")
    else:
            result = (zmienna / zmiennaB)
            print("Wynik:", result)