# David Soldatic (Nino Telefonino)

def validiraj_broj_telefona(broj):

    # 1. poz.brojevi
    fiksni = {
        "01": "Grad Zagreb i Zagrebačka županija",
        "020": "Dubrovačko-neretvanska županija",
        "021": "Splitsko-dalmatinska županija",
        "022": "Šibensko-kninska županija",
        "023": "Zadarska županija",
        "031": "Osječko-baranjska županija",
        "032": "Vukovarsko-srijemska županija",
        "033": "Virovitičko-podravska županija",
        "034": "Požeško-slavonska županija",
        "035": "Brodsko-posavska županija",
        "040": "Međimurska županija",
        "042": "Varaždinska županija",
        "043": "Bjelovarsko-bilogorska županija",
        "044": "Sisačko-moslavačka županija",
        "047": "Karlovačka županija",
        "048": "Koprivničko-križevačka županija",
        "049": "Krapinsko-zagorska županija",
        "051": "Primorsko-goranska županija",
        "052": "Istarska županija",
        "053": "Ličko-senjska županija"
    }

    mobilni = {
        "091": "A1 Hrvatska",
        "092": "Tomato",
        "095": "Telemach",
        "097": "bonbon",
        "098": "Hrvatski Telekom",
        "099": "Hrvatski Telekom"
    }

    posebni = {
        "0800": "Besplatni pozivi",
        "060": "Komercijalni pozivi",
        "061": "Glasovanje telefonom",
        "064": "Usluge s neprimjerenim sadržajem",
        "065": "Nagradne igre",
        "069": "Usluge namijenjene djeci",
        "072": "Jedinstveni pristupni broj"
    }

    # 2. ocisti broj od nepotrebnih znakova
    cisti_broj = ""
    for znak in broj:
        if znak.isdigit() or znak == '+':
            cisti_broj += znak

    # 3. Ukloni međunarodne prefikse (+385, 00385, (385))
    if cisti_broj.startswith("+385"):
        cisti_broj = cisti_broj[4:]
    elif cisti_broj.startswith("00385"):
        cisti_broj = cisti_broj[5:]
    elif cisti_broj.startswith("385"):
        cisti_broj = cisti_broj[3:]

    if not cisti_broj.startswith("0"):
        cisti_broj = "0" + cisti_broj

    # 4. Pronađi poz.broj
    pozivni_broj = None
    vrsta = None
    mjesto = None
    operater = None

    # prvo posebne usluge (jer mogu biti 4 znamenke)
    for kod in posebni:
        if cisti_broj.startswith(kod):
            pozivni_broj = kod
            vrsta = "posebne usluge"
            mjesto = None
            operater = None
            break

    # ako nije posebna usluga
    if pozivni_broj is None:
        for kod in mobilni:
            if cisti_broj.startswith(kod):
                pozivni_broj = kod
                vrsta = "mobilna mreža"
                mjesto = None
                operater = mobilni[kod]
                break

    # ako nije mobilni
    if pozivni_broj is None:
        for kod in fiksni:
            if cisti_broj.startswith(kod):
                pozivni_broj = kod
                vrsta = "fiksna mreža"
                mjesto = fiksni[kod]
                operater = None
                break

    # 5. Izdvoji ost.broja
    if pozivni_broj is not None:
        broj_ostatak = cisti_broj[len(pozivni_broj):]
    else:
        broj_ostatak = cisti_broj

    # 6. Val. dulj.broja
    validan = False
    if vrsta == "fiksna mreža" and len(broj_ostatak) in [6, 7]:
        validan = True
    elif vrsta == "mobilna mreža" and len(broj_ostatak) in [6, 7]:
        validan = True
    elif vrsta == "posebne usluge" and len(broj_ostatak) == 6:
        validan = True

    # 7. Sastavi rezultat
    rezultat = {
        "pozivni_broj": pozivni_broj,
        "broj_ostatak": broj_ostatak,
        "vrsta": vrsta,
        "mjesto": mjesto,
        "operater": operater,
        "validan": validan
    }

    return rezultat


# testiranje
unos = input("Unesite broj telefona: ")
rezultat = validiraj_broj_telefona(unos)
print(rezultat)