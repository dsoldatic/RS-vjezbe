from fakultet.student import Student
from fakultet.podaci import razredi_studenti

# 1. 
studenti_objekti = []

# 2. 
for element in razredi_studenti:
    naziv_razreda = element["razred"]
    
    for student_dict in element["studenti"]:
        dijelovi_imena = student_dict["ime_prezime"].split(" ", 1)
        ime = dijelovi_imena[0]
        prezime = dijelovi_imena[1] if len(dijelovi_imena) > 1 else ""
        
        ocjene = {k["naziv"]: k["ocjena"] for k in student_dict["kolegiji"]}
        
        novi_student = Student(ime, prezime, naziv_razreda, ocjene)
        studenti_objekti.append(novi_student)

# 3. 
print("--- Popis studenata ---")
for s in studenti_objekti:
    print(f"Student: {s.ime} {s.prezime}, Razred: {s.razred}, Ocjene: {s.kolegij_ocjene}")

# 4. Testiranje 
if studenti_objekti:
    prvi_student = studenti_objekti[0]
    print(f"\nProsjek ({prvi_student.ime}): {prvi_student.prosjek_ocjena()}")

    try:
        print("Mijenjam razred...")
        prvi_student.promjena_razreda("1B")
        print(f"Uspješno! Novi razred: {prvi_student.razred}")
    except ValueError as e:
        print(f"Greška: {e}")