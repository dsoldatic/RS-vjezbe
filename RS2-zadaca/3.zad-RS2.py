# Zadaci 3. Zadaci za vježbu - lambda izrazi, funkcije 
# višeg reda i comprehension sintaksa

# RS2 David Soldatic
## Zadatak 1: Lambda izrazi

# 1. Kvadriranje broja:
kvadriraj = lambda x: x ** 2
print(kvadriraj(5))

# 2. Zbroji pa kvadriraj:
zbroji_pa_kvadriraj = lambda a,b: (a + b) ** 2
print(zbroji_pa_kvadriraj(2, 3))

# 3. Kvadriraj duljinu niza:
kvadriraj_duljinu = lambda x: len(x) ** 2
print(kvadriraj_duljinu("Igor"))        ## 16

# 4. Pomnoži vrijednost s 5 pa potenciraj na x:
pomnozi_i_pontenciraj = lambda x,y: (y*5) ** x
print(pomnozi_i_pontenciraj(3,4))       ## 8000

# 5. Vrati True ako je broj paran, inače vrati None:
paran_broj = lambda x: "True" if x % 2 == 0 else "None"
print(paran_broj(6))


## Zadatak 2: Funkcije višeg reda

# 1. Koristeći funkciju map , kvadrirajte duljine svih nizova u listi:
nizovi = ["jabuka", "kruška", "banana", "naranča"]
kvadrirane_duljine = list(map(lambda niz: len(niz) ** 2, nizovi))
print(kvadrirane_duljine)

# 2. Koristeći funkciju filter , filtrirajte samo brojeve koji su veći od 5:
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
veci_od_5 = list(filter(lambda broj: broj > 5, brojevi))
print(veci_od_5)

# 3. Koristeći odgovarajuću funkciju višeg reda i lambda izraz (bez comprehensiona), pohranite u varijablu 
# transform rezultat kvadriranja svih brojeva u listi gdje rezultat mora biti rječnik gdje su ključevi
# originalni brojevi, a vrijednosti kvadrati tih brojeva:
brojevi = [10, 5, 12, 15, 20]
transform = dict(map(lambda broj: (broj, broj ** 2),brojevi))
print(transform) 

# 4. Koristeći funkcije all i map , provjerite jesu li svi studenti punoljetni:
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19},
{"ime": "Marko", "prezime": "Marković", "godine": 22},
{"ime": "Ana", "prezime": "Anić", "godine": 21},
{"ime": "Petra", "prezime": "Petrić", "godine": 13},
{"ime": "Iva", "prezime": "Ivić", "godine": 17},
{"ime": "Mate", "prezime": "Matić", "godine": 18}
]
svi_punoljetni = all(map(lambda student: student["godine"] > 18, studenti))
print(svi_punoljetni)

# 5. Definirajte varijablu min_duljina koja će pohranjivati int . Koristeći odgovarajuću funkciju višeg reda
# i lambda izraz, pohranite u varijablu duge_rijeci sve riječi iz liste rijeci koje su dulje od
# min_duljina :

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]
min_duljina = int(input("Unesite minimalnu duljinu riječi: "))
duge_rijeci = list(filter(lambda rijec: len(rijec) > min_duljina,rijeci))
print(duge_rijeci)



## Zadatak 3: Comprehension sintaksa
#1. Koristeći list comprehension, izgradite listu parnih kvadrata brojeva od 20 do 50:
parni_kvadrati = [x ** 2 for x in range(20,51) if x % 2 == 0]
print(parni_kvadrati)

# 2. Koristeći list comprehension, izgradite listu duljina svih nizova u listi rijeci , ali samo za nizove koji
# sadrže slovo a
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]
duljine_sa_slovom_a = [len(slovo) for slovo in rijeci if "a" in slovo]
print(duljine_sa_slovom_a) # [6, 3, 6, 8, 9, 8, 6, 17]

# 3. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi brojevi od 1 do 10, a vrijednosti
# kubovi tih brojeva, ali samo za neparne brojeve, za parne brojeve neka vrijednost bude sam broj

kubovi = [{broj: broj ** 3} if broj % 2 != 0 else broj for broj in range(1,11)]
print(kubovi)

# 4. Koristeći dictionary comprehension, izgradite rječnik iteriranjem kroz listu brojeva od 50 do 500 s
# korakom 50, gdje su ključevi brojevi, a vrijednosti su korijeni tih brojeva zaokruženi na 2 decimale:
import math
korijeni = {broj: round(math.sqrt(broj), 2) for broj in range(50, 501, 50)}
print(korijeni)

# 5. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi prezimena studenata, a vrijednosti
# su zbrojeni bodovi, iz liste studenti
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
{"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
{"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
{"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
{"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
{"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]
zbrojeni_bodovi = [{student["prezime"]: sum(student["bodovi"])} for student in studenti]
print(zbrojeni_bodovi)

import math

# 6. Dictionary comprehension: ključevi su brojevi od 1 do 10,
# a vrijednosti su liste faktorijela svih brojeva do tog broja
faktorijeli = {broj: [math.factorial(i) for i in range(1, broj + 1)] for broj in range(1, 11)}

print(faktorijeli)
