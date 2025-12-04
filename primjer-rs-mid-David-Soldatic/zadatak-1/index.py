import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))
from studenti import razredi_studenti

# 1.2
def dohvati_studente_iz_razreda(razredi_studenti: list, naziv_razreda: str) -> list:
    imena = []
    for element in razredi_studenti:
        if element["razred"] == naziv_razreda:
            for student in element["studenti"]:
                imena.append(student["ime_prezime"])
    return imena

# 1.3
def prosjek_studenta(razredi_studenti: list, ime_prezime: str) -> float:
    for element in razredi_studenti:
        for student in element["studenti"]:
            if student["ime_prezime"] == ime_prezime:
                ocjene = [k["ocjena"] for k in student["kolegiji"]]
                if not ocjene:
                    return 0.0
                return sum(ocjene) / len(ocjene)
    return None

# 1.4 
broj_studenata = [(element["razred"], len(element["studenti"])) for element in razredi_studenti]

# 1.5 
studenti_1B = [
    s["ime_prezime"] 
    for element in razredi_studenti 
    if element["razred"] == "1B" 
    for s in element["studenti"]
]

if __name__ == "__main__":
    # Testiranje
    print(dohvati_studente_iz_razreda(razredi_studenti, "1A"))
    print(prosjek_studenta(razredi_studenti, "Ana Horvat"))
    print(broj_studenata)
    print(studenti_1B)