imię = input("Jak masz na imię?\n")
print("Witaj",imię, "!Bardzo się cieszę, że jesteś tutaj ze mną. Jest piękny słoneczny dzień, jestem szczęśliwa,\nponieważ uczę się programowania i coraz bardziej mi się to podoba!")
samopoczucie = input("A Ty? Jak się dzisiaj czujesz? ")
print("Twoja odpowiedź to:", samopoczucie.upper())
znaki=len(samopoczucie)
if znaki == 1:
    print("Użyłeś w swojej wypowiedzi:", znaki, "znak")
if znaki >= 1 and znaki <= 4 and znaki >=22 and znaki <= 24:
    print ("Użyłeś w swojej wypowiedzi:\n", znaki, "znaki")
if znaki >= 5:
    print ("Użyłeś w swojej wypowiedzi:\n", znaki, "znaków")
slowa = len(samopoczucie.split())
if slowa == 1:
    print (slowa, "słowo")
if slowa >= 2 and znaki <=4:
    print (slowa,"słowa")
if znaki >= 5:
    print (slowa, "słów")
