lentokentat = {}

while True:
    print("\nValitse toiminto:")
    print("1 - Lisää lentokenttä")
    print("2 - Hae lentokenttä")
    print("3 - Lopeta")

    valinta = input("Valinta: ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentokentän nimi: ")
        lentokentat[icao] = nimi

    elif valinta == "2":
        icao = input("Anna ICAO-koodi: ")
        if icao in lentokentat:
            print("Lentokenttä:", lentokentat[icao])
        else:
            print("Koodia ei löytynyt")

    elif valinta == "3":
        print("Ohjelma lopetettu")
        break

    else:
        print("Virheellinen valinta")