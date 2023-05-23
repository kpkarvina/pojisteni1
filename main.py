from insured import Pojisteny
from insured_manager import ManagerPojisteni

def vytvorit_pojisteneho():
    jmeno = input("Zadejte jméno: ")
    prijmeni = input("Zadejte příjmení: ")
    vek = int(input("Zadejte věk: "))
    telefon = input("Zadejte telefonní číslo: ")
    return Pojisteny(jmeno, prijmeni, vek, telefon)

def zobrazit_vsechny_pojistene(insurance_manager):
    pojisteni_list = insurance_manager.ziskat_vsechny_pojistene()
    for pojisteny in pojisteni_list:
        print(pojisteny)

def vyhledat_pojisteneho_podle_jmena(insurance_manager):
    jmeno = input("Zadejte jméno: ")
    prijmeni = input("Zadejte příjmení: ")
    pojisteny = insurance_manager.vyhledat_pojisteneho(jmeno, prijmeni)
    if pojisteny:
        print(pojisteny)
    else:
        print("Pojistný nenalezen")

def smazat_pojisteneho_podle_jmena(insurance_manager):
    jmeno = input("Zadejte jméno: ")
    prijmeni = input("Zadejte příjmení: ")
    if insurance_manager.smazat_pojisteneho(jmeno, prijmeni):
        print("Pojistný byl úspěšně smazán")
    else:
        print("Pojistný nenalezen nebo chyba při mazání")

def main():
    insurance_manager = ManagerPojisteni()
    while True:
        print("\nEvidenční aplikace pro pojistné události")
        print("1. Vytvořit pojistného")
        print("2. Zobrazit všechny pojistné")
        print("3. Vyhledat pojistného podle jména")
        print("4. Smazat pojistného podle jména")
        print("5. Konec")
        volba = input("Zadejte číslo volby: ")
        if volba == "1":
            pojisteny = vytvorit_pojisteneho()
            insurance_manager.pridat_pojisteneho(pojisteny)
            print("Pojistný úspěšně vytvořen!")
        elif volba == "2":
            zobrazit_vsechny_pojistene(insurance_manager)
        elif volba == "3":
            vyhledat_pojisteneho_podle_jmena(insurance_manager)
        elif volba == "4":
            smazat_pojisteneho_podle_jmena(insurance_manager)
        elif volba == "5":
            break
        else:
            print("Neplatná volba")

if __name__ == "__main__":
    main()