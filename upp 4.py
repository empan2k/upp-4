while True:
    text = input("Skriv något (q för att avsluta): ")

    if text == "q":
        break

    print(text)

text = input("Skriv något: ")

for i in range(10):
    print(text)

for i in range(1, 11):
    print(i)

y = int(input("Skriv ett heltal y: "))

for i in range(1, y + 1):
    print(i)

for tabell in range(1, 11):
    print("Tabell", tabell)

    for tal in range(1, 11):
        print(tabell, "x", tal, "=", tabell * tal)

    print()

bas = int(input("Skriv basen: "))
exponent = int(input("Skriv exponenten: "))

resultat = 1

for i in range(exponent):
    resultat = resultat * bas

print(bas, "upphöjt till", exponent, "=", resultat)