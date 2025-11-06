# David Soldatic (RS1)

# 7. Zadatak
lozinka = str(input("Unesite lozinku:"))
if len(lozinka) < 8 or len(lozinka) > 15:
    print("Lozinka mora sadržavati između 8 i 15 znakova")
elif not any(char.isupper() for char in lozinka) or not any(char.isdigit() for char in lozinka):
    print ("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj.")
elif "password" in lozinka.lower() or lozinka in lozinka.lower():
    print ("Lozinka ne smije sadržavati riječi password ili lozinka.")
else:
    print("Lozinka je dovoljno jaka!")

# 8. Zadatak  
def filtriraj_parne(lista):
    nova_lista = []
    for broj in lista:
        if broj % 2 == 0:
            nova_lista.append(broj)
    return(nova_lista)

lista = [1,2,3,4,5,6,7,8,9,10]
print (filtriraj_parne(lista))

# 9. zadatak
def ukloni_duplikate(lista):
    nova_lista = []
    for broj in lista:
        if broj not in nova_lista:
            nova_lista.append(broj)
    return(nova_lista)

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))


# 10. zadatak
def brojanje_rijeci(tekst):
    rijeci = tekst.split()
    counter = {}
    for rijec in rijeci:
        if rijec in counter:
            counter[rijec]+= 1
        else:
            counter[rijec] = 1
    return(counter)
    
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print (brojanje_rijeci(tekst))


# 11. zadatak
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rjecnik = {"Parni": [], "Neparni": []}
def grupiraj_po_paritetu(lista):
    for broj in lista:
        if broj % 2 == 0:
            rjecnik["Parni"].append(broj) 
        else: # odd number
            rjecnik["Neparni"].append(broj)
    return(rjecnik)

print(grupiraj_po_paritetu(lista))


# 12. zadatak
rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
novi_rjecnik = {}
def obrni_rjecnik(rjecnik):
    for kljuc, vrijednost in rjecnik.items():
        novi_rjecnik[vrijednost] = kljuc
    return(novi_rjecnik)

print(obrni_rjecnik(rjecnik))


# 13.1 zadatak
lista = [ 1,2,3,4,5,6,7,8,9,10]
tuple = ()
def prvi_i_zadnji(lista):
    tuple = (lista[0], lista[-1])
    return(tuple)
print(prvi_i_zadnji(lista))


# 13.2 zadatak
lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

def maks_i_min(lista):
    najveci_broj = lista[0]
    najmanji_broj = lista[0]
    brojac = 0 

    for broj in lista:
        if broj > najveci_broj:
            najveci_broj = broj
        if broj < najmanji_broj:
            najmanji_broj = broj
        brojac += 1  

    return (najveci_broj, najmanji_broj)

print(maks_i_min(lista))  


# 13.3 zadatak 
skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

def presjek(skup_1, skup_2):
    return (skup_1.intersection(skup_2))

print(presjek(skup_1,skup_2))


# 14.1 zadatak
def isPrime(broj):
    for i in range(2,int(broj**0.5)+1):
        if broj%i==0:
            return False
    return True

print(isPrime(7))
print(isPrime(10))


# 14.2 zadatak 
def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

print(primes_in_range(1, 10))



# 15. zadatak
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def count_vowels_consonants(tekst):
    vowels = 0
    consonants = 0
    for i in range(0, len(tekst)):
         if (tekst[i] >= 'a' and tekst[i] <= 'z') or (tekst[i] >= 'A' and tekst[i] <= 'Z'):
            znak = tekst[i].lower()
            if znak in 'aeiou':
                vowels += 1
            else:
                consonants += 1
    return {"vowels": vowels, "consonants": consonants}

print(count_vowels_consonants(tekst))