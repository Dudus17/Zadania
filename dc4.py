imię = input("Jak masz na imię?\n")
print("Witaj",imię,"\nBardzo się cieszę, że jesteś tutaj ze mną. Jest piękny słoneczny dzień, jestem szczęśliwa,\nponieważ uczę się programowania i coraz bardziej mi się to podoba!")
samopoczucie = input("A Ty? Jak się dzisiaj czujesz? ")
print("\nTwoja odpowiedź to:", samopoczucie.upper(), "\n")
znaki=len(samopoczucie)
slowa = len(samopoczucie.split())

from prettytable import PrettyTable

# Tworzenie obiektu PrettyTable
table = PrettyTable()

# Definiowanie kolumn
table.field_names = ["Kategoria", "Output"]

# Dodawanie danych do tabeli
table.add_row(["Użyłeś słów", slowa])
table.add_row(["Użyłeś znaków", znaki])

# Wyświetlenie tabeli
print(table)