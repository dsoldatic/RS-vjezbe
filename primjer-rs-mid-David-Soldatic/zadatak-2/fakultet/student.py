from .podaci import razredi_studenti

class Student:
    def __init__(self, ime, prezime, razred, kolegij_ocjene):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.kolegij_ocjene = kolegij_ocjene

    # 2.3
    def prosjek_ocjena(self):
        ocjene = self.kolegij_ocjene.values()
        if not ocjene:
            return 0.0
        return round(sum(ocjene) / len(ocjene), 1)

    # 2.4
    def promjena_razreda(self, novi_razred):
        dozvoljeni = {r["razred"] for r in razredi_studenti}
        
        if novi_razred not in dozvoljeni:
            raise ValueError(f"Razred {novi_razred} nije dopušten.")
        
        self.razred = novi_razred