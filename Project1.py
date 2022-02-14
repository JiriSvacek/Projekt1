TEXTS = ("Klasické pasáže Lorem Ipsum z 16. století jsou reprodukovány níže",
         " Jeho původ má kořeny v klasické latinské literatuře z roku 45 "
         "před Kristem, což znamená, že je více jak 2000 let staré.",
         "Používá totiž slovník více jak 200 latinských slov, která "
         "jsou kombinována do vět tak, aby text vypadal rozumně.")

prihlasovaci_udaje = {"bob": "123",
                      "ann": "pass123",
                      "mike": "password123",
                      "liz": "pass123"
                      }

# Proměné
prihlasen = False
cislo_int = 0
pocet_cisel = 0
pocet_male = 0
pocet_velke = 0
pocet_slov = 0
pocet_zacatek = 0
suma_cisel = 0
delky_slov = {}
oddelovac = "-" * 40

# Vyžádání jména a hesla
jmeno = input("Zadej jméno: ")
heslo = input("Zadej heslo: ")

# Kontrola přihlašovacích údajů
for prihlaseni in prihlasovaci_udaje:
    if prihlaseni in jmeno:
        if prihlasovaci_udaje.get(prihlaseni) == heslo:
            prihlasen = True
        break

if not prihlasen:
    print("Unregistered user or wrong password, terminating the program..")
    quit()

print(oddelovac)
print(f"Welcome to the app, {jmeno}.\nWe have 3 texts to be analyzed.")
print(oddelovac)

# Při správně zadaných přístupových údajích, požaduje zadat číslo textu
cislo_str = input("Enter a number btw. 1 and 3 to select: ")

if not cislo_str.isnumeric():
    print("Not a number, terminating the program..")
    quit()
else:
    cislo_int = int(cislo_str)
    if not 1 <= cislo_int <= 3:
        print("Wrong number, terminating the program..")
        quit()

# Vyber textu a výpočet
vyber = TEXTS[cislo_int - 1].split()

for slovo in vyber:
    ciste = slovo.strip(".,")
    if ciste.isalpha():
        pocet_slov += 1

        if not (len(ciste) in delky_slov):
            delky_slov.setdefault(len(ciste), 1)
        else:
            delky_slov[len(ciste)] += 1

        if ciste.isupper():
            pocet_velke += 1
        elif ciste.istitle():
            pocet_zacatek += 1
        else:
            pocet_male += 1

    elif ciste.isnumeric():
        pocet_cisel += 1
        suma_cisel += int(ciste)
    elif ciste[0] == "-" and ciste[1:].isnumeric():
        pocet_cisel += 1
        suma_cisel -= int(ciste[1:])

serazeno = sorted(delky_slov.items())

# Vypsání údajů
print(oddelovac)
print(f"""There are {pocet_slov} words in the selected text.
There are {pocet_zacatek} titlecase words.
There are {pocet_velke} uppercase words.
There are {pocet_male} lowercase words.
There are {pocet_cisel} numeric strings.
The sum of all the numbers {suma_cisel}""")
print(oddelovac)

print('{:>3}| {:^10s} |{:>3}'.format("LEN", "OCCURENCES", "NR."))

for p, m in serazeno:
    hvezdy = "*" * m
    print('{:>3}| {:<10s} |{:>3}'.format(p, hvezdy, m))

print(oddelovac)
