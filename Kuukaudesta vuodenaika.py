# Lista, jossa indeksit 0–11 vastaavat kuukausia 1–12
vuodenajat = [
    "talvi", "talvi", "kevät",
    "kevät", "kevät", "kesä",
    "kesä", "kesä", "syksy",
    "syksy", "syksy", "talvi"
]

kk = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kk <= 12:
    print("Vuodenaika on:", vuodenajat[kk - 1])
else:
    print("Virheellinen kuukausi")