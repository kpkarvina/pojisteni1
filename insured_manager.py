class ManagerPojisteni:
    def __init__(self):
        self.pojisteni_list = []

    def pridat_pojisteneho(self, pojisteny):
        self.pojisteni_list.append(pojisteny)

    def ziskat_vsechny_pojistene(self):
        return self.pojisteni_list

    def vyhledat_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.pojisteni_list:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny
        return None

    def smazat_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.pojisteni_list:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                self.pojisteni_list.remove(pojisteny)
                return True
        return False