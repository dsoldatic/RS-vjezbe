# Zadaci 
# 6. Zadaci za vježbu - Klase, objekti, moduli i paketi

# RS2 2.dio David Soldatic

## Zadatak 4: Klase i objekti

# 1. Definirajte klasu Automobil s atributima marka , model , godina_proizvodnje i kilometraža .
# Dodajte metodu ispis koja će ispisivati sve atribute automobila.
# Stvorite objekt klase Automobil s proizvoljnim vrijednostima atributa i pozovite metodu ispis .
# Dodajte novu metodu starost koja će ispisivati koliko je automobil star u godinama, trenutnu
# godine 

from datetime import datetime
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        return f"Marka automobila: {self.marka}, model: {self.model}, godina proizvodnje: {self.godina_proizvodnje}, kilometraža: {self.kilometraza}"
    def starost(self):
        trenutna_godina = datetime.now().year
        return f"Automobil je star {trenutna_godina - self.godina_proizvodnje} godina."    

automobil = Automobil("Audi","automatik", 2020,85400)

print(automobil.ispis())

# 2. Definirajte klasu Kalkulator s atributima a i b . Dodajte metode zbroj , oduzimanje , mnozenje ,
# dijeljenje , potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i b.
class Kalkulator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b
    def dijeljenje(self):
        return self.a / self.b
    def potenciranje(self):
        return self.a ** self.b
    def korijen(self):
        return self.a ** 0.5
    
kalkulator = Kalkulator(10,5)
print("Zbroj:", kalkulator.zbroj())
print("Oduzimanje:", kalkulator.oduzimanje())
print("Množenje:", kalkulator.mnozenje())
print("Dijeljenje:", kalkulator.dijeljenje())
print("Potenciranje:", kalkulator.potenciranje())
print("Korijen:",kalkulator.korijen())


# 3. zadatak

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)
        

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
{"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
{"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
{"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
{"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
{"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]
studenti_objekti = [Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti]
najbolji_student = max(studenti_objekti, key=lambda student: student.prosjek())
print(f"Najbolji student: {najbolji_student.ime} {najbolji_student.prezime} s prosjekom {najbolji_student.prosjek()}")


# 4 zadatak
import math
class Krug:
    def __init__(self, r):
        self.r = r
        self.pi = math.pi
    def opseg(self):
        return 2 * self.pi * self.r
    def povrsina(self):
        return self.pi * self.r ** 2

radijus = 7 
moj_krug = Krug(radijus)

print(f"Radijus je {radijus}, a opseg je: {moj_krug.opseg():.2f}")
print(f"Radijus je {radijus}, a površina  je: {moj_krug.povrsina():.2f}")

# 5. Definirajte klasu Radnik s atributima ime , pozicija , placa . Dodajte metodu work koja će ispisivati
# "Radim na poziciji {pozicija}".
# Dodajte klasu Manager koja nasljeđuje klasu Radnik i definirajte joj atribut department . Dodajte
# metodu work koja će ispisivati "Radim na poziciji {pozicija} u odjelu {department}".
# U klasu Manager dodajte metodu give_raise koja prima parametre radnik i povecanje i
# povećava plaću radnika ( Radnik ) za iznos povecanje .
# Definirajte jednu instancu klase Radnik i jednu instancu klase Manager i pozovite metode work i give_raise .
class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    def work(self):
        print(f"Radim na poziciji {self.pozicija}.")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}.")
    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"Povišena plaća za radnika {radnik.ime}: nova plaća je {radnik.placa}.")

rad = Radnik("Ivan", "Programer", 5000)
man = Manager("Ana", "Voditelj", 8000, "IT")
rad.work()
man.work()

man.give_raise(rad, 1000)



# Zadatak 5: Moduli i paketi

