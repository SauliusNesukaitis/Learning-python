#Apžvelgsime
# Pagrindines oficialias Python programuotojų rekomendacijas
# Rekomendacijos kintamųjų ir kitų programos elementų sintaksei
# Kada nerekomenduojama “aklai” sekti rekomendacijų
# Komentarai, jų paskirtis ir rašymo taisyklės
# Tarpai ir “tab” simbolis

# Kodėl yra pateikiamos rekomendacijos programavimo stiliui?
# Dėl to, kuris kodą rašys
# Dėl to, kuris kodą skaitys
# Dėl bendrų darbo grupių, kai kelių skirtingų programuotojų darbai yra sujungiami į bendrą sistemą

# Kada rekomendacijas REKOMENDUOJAMA ignoruoti?
# Tada, kai jų laikantis parašytas kodas tampa sunkiau skaitomas/suprantamas
# Jei kodas jau yra veikiantis , naudojamas ir nėra didelio poreikio jį modifikuoti
# Kai laikytis rekomendacinių gairių yra per sudėtinga siekiant suderinti kelių 
# programuotojų atskirus kodus.
# Kai kodas yra kurtas ankstesne Python versija, neatitinkančia rekomendacijų

# Rekomendacijos pavadinimams
# Pavadinimas turi prasidėti raide
# Pavadinimas negali prasidėti skaičiumi
# Pavadinimo nerekomenduojama iš vienos raidės “l” (L mažosios) ir “o” 
# simbolio, pvz., o=2 gali atrodyti, kad nulį bandome pervardinti į du.
# Pavadinimų nerekomenduojama dubliuoti su standartinių funkcijų 
# pavadinimais, nes ne tik patys galite susipainioti, 
# bet ir programa “suinterpretuoti” klaidingai


# Rekomendacijos pavadinimų stiliui
# Funkcija: 
# Naudoti mažąsias raides žodyje. Jei funkcijos pavadinimas iš kelių žodžių, juos atskirti “_” simboliu
# function, my_function
# Kintamasis:
# Naudoti mažąsias raides, jei kintamąjį sudaro ne vienas žodis, atskirti “_” simboliu
# x, var, my_var
# Klasė:
# Pavadinimą pradėti iš didžiosios raidės. 
# Jei pavadinimą sudaro keli žodžiai, kiekvieną pradėti didžiąja raide, 
# bet neatskirinėti nei tarpu, nei simboliu
# Model, MyClass, KatesKlase t.t.
# Metodas
# Pavadinimą pradėti mažąja raide, jei yra keli žodžiai, atskirti “_” simboliu
# class_method, method
# Modulis
# Pavadinimą pradėti mažąja raide, jei yra keli žodžiai, atskirti “_” simboliu
# module.py, my_module.py
# Konstanta 
# Visos raidės didžiosios. Jei konstantą sudaro ne vienas žodis, atskirti “_” simboliu
# CONSTATNT, MY_CONSTANT, MY_LONG_CONSTANT
# Rinkinys (pacage)
# Naudoti mažąsias raides. Jei pavadinimą sudaro daugiau nei vienas žodis, neatskirinėti jų nei simboliu, nei tarpu
# pacage, mypacage

# Kintamųjų pavadinimų pasirinkimas
# Priklausomai nuo situacijos, kai kurie pasirinkimai gali būti klaidinantys. 
# Pvz.,įprasta kintamuosius “pavadinti” x, y. 
# Tačiau turint matematines funkcijas, gali būti dviprasmybių dėl argumento paskirties.
# Visada reikia stengtis sudaryti prasmingą pagal funkcionalumą pavadinimą.
# Tarkime, norime atspausdinti String tipo kintamųjų reikšmes (pvz., vardą ir
# pavardę), atskirtas tarpo simboliu. 
# Žinant kintamųjų paskirtį, nerekomenduojama jų “pavadinti” x, y. Pvz.

vardas_pavarde = "Antanas Kaunietis" #geras pvz
n = "Gintare Lauciene" #blogas pvz

# Kodo išdėstymo rekomendacijos
# Patariama išlaikyti lygiagrečią tvarką tarp klasių taip, kad būtų galima lengvai 
# identifikuoti atskiras klases. Tai yra, klasės lygiuojamos vertikaliai, o tarp jų 
# paliekamas tarpas. Pvz.,

class PirmaKlase:
    pass
class AntraKlase:
    pass
class TreciaKlase:
    return None

 # Jei klasę sudaro kelios funkcijos, patartina tarp jų palikti vieną eilutę tuščią, pvz.,   

class PirmaKlase:
    def pirmas_metodas(self):
        return None
    
    def antras_metodas(self):
        return None

# Lygiai taip pat, jei funkcijoje vykdomi keli procesai prieš grąžinant reikšmę.
# Procesus galima atskirti tuščia eilute tam, kad būtų nesudėtinga suprasti kur
# konkretaus proceso pradžia ir pabaiga

# Kodo eilutės ilgis
# Pagal pateiktas rekomendacijas, eilutės ilgis neturi viršyti 79 simbolių. 
# Tai yra tik rekomendacija, nes ne visais atvejais simbolių skaičių eilutėje galima mažinti.
# Kodas yra teisingas, jei jis yra perkeliamas apskliaudus sklaustukais, t.y. 

def funkcija(argumentas1, argumentas2,
            argumentas3, argumentas4):
            return None

# Jei skliaustų naudoti neįmanoma, kodas gali būti perkeliamas į kitą eilutę “\” 
# simbolio pagalba:
from mypkg import pavz_1, \
     pvz2 , pvz3

# Aritmetinis veiksmas perkeliamas taip, kad operatorius yra naujoje eilutėje, t.y.
veiksmas = (kintamasis+
            kintamasis2-
            kintamasis3) # NEREKOMENDUOJAMA

veiksmas = (kintamasis
            +kintamasis2
            -kintamasis3)

# “Tab” ar “Space”
# Tarpo simboliui reikia naudoti tik “Space” klavišą ir nenaudoti “Tab”. 
# Naudojant ankstesnę Python versiją, jei naudojote ir “Tab” ir “Space”, jūs nematysite klaidos. 
# Tam, kad patikrinti klaidas, paleidžiant kodą per komandinį langą, reikia pridėti simbolį “-t”.
# PVZ: KOMANDINIAME LANGE
# $ python2 -t code.py
# code.py:inconsistent use of tabs and spaces in indentation
# Tokiu atveju, programos interpretatorius spausdins pranešimą apie “Tab” 
# naudojimą vietoj tarpo simbolio
# Python 3 versijoje maišyti “Tab” ir “Space” negalima.
#  Jei yra tokia klaida, programos interpretatorius iš karto meta pranešimą, pvz.,
# $ python3 code.py
# File "code.py", line3
# print(i,j)
#^
#TabError: inconsistent use of tabs and spaces in indentation

# Komentarų rašymas
# Komentarų rašymas programoje leidžia greitai ir lengvai ją suprasti ir paaiškinti. 
# Komentaras rašomas po “#” simbolio.

# Kelios rekomendacijos komentarų rašymui:
# Komentaras eilutėje neturėtų būti ilgesnis nei 72 simboliai. 
# Jei komentaras ilgesnis, perkelti jį į kitą eilutę, kur pirmas simbolis “#”.
# Komentaras pradedamas didžiąja raide.
# Komentare suformuluotas pilnas aiškus konkretus sakinys.
# Nepamiršti atnaujinti komentarą, jei programoje buvo padaryti pakeitimai
# Sudėtingą programą rekomenduojama komentuoti atskiromis sekcijomis. 
# Tai yra, trumpus komentarus rašyti prieš konkretų procesą.
# Kartais vienoje sekcijoje reikalingi net keli nesusiję komentarai. 
# Tokiu atveju, jie atskiriami tuščia eilute, kurios pirmas simbolis yra “#”.

# Vidiniai komentarai rašomi eilutės gale. 
# Jų pagalba lengviau prisiminti arba kitiems paaiškinti konkrečios eilutės svarba.
# Vidinių komentarų rašymo rekomendacijos:
# Komentarus rašyti trumpus ir konkrečius
# Nerašyti komentarų ten, kur kodas yra akivaizdus ir aiškus
# Komentaro simbolį dėti po dviejų tarpo simbolių
# Po komentaro simbolio prieš patį komentarą palikti vieną tarpo simboli
# Kartais vidinių komentarų galime išvengti teisingai pavadindami funkcijas, 
# modulius ir t.t., iš kurių pavadinimo bus aišku, kas bus daroma.

# Komentarų dokumentacijai rašymo rekomendacijos
# Dokumentacijai programos kode naudojamos trys viengubos arba dvigubos kabutės.
# Kabutės rašomos ir prieš dokumentaciją, ir po jos.
# Skirtingai nei komentarų rašyme, dokumentacijoje, keliant tekstą į kitą eilutę, trijų kabučių
# papildomai nereikia. Dokumentacija rašoma nuo vienų iki kitų kabučių.
#arba
'''
Dokumentacija
'''
# arba
def funkcija():
"""
Dokumentacija
"""
    veiksmai
# Turint vienos eilutės dokumentaciją, tiek pradžios, tiek pabaigos kabutės rašomos toje pat
# eilutėje. Jei dokumentaciją sudaro daugiau eilučių, pabaigos kabutės yra naujoje eilutėje

# Tarpo simbolis tarp operatorių
# Nerekomenduojama dėti tarpo simbolių prieš ir po šių operatorių:
# Nerekomenduojama dėti tarpo simbolių prieš ir po šių operatorių:
# Priskyrimo (=, +=, -=, and so forth)
# Lyginimo (==, !=, >, <. >=, <=) and (is, is not, in, not in)
# Loginių (and, not, or)
# Jei vienoje eilutėje yra ne vienas veiksmas, mažesnio prioriteto veiksmas
# atskiriamas tarpo simboliu.
y = x**2 + 5
z = (x+y) * (x-y)
# Tarpo simboliu atskiriama ir dviguba “if” sąlyga:
if x>5 and x%2==0:
# Tarpai apibrėžiant masyvus ir matricas
# Jei tik galima, reikia vengti tarpo simbolio aprašant kintamuosius
# Norint aprašyt eilutes ir stulpelius, galima dėti tarpo simbolį iš abiejų “:” pusių
# Pagrindinis reikalavimas, kad visur būtų išlaikyta ta pati tvarka.

# Bendros programavimo gairės padeda lengviau suderinti skirtingų
# programuotojų modulius ir programas į vieną sistemą
# Laikantis tvarkingo kodo rašymo išvengsime “nesuvokiamų” klaidų kai
# sintaksė teisinga, o programa neveikia, arba veikia nekorektiškai
# Tarpo simbolis irgi yra simbolis, todėl kai kuriais atvejais programa interpretus kaip klaidą
# Komentarai rašomi tam, kad lengviau būtų prisiminti, kas buvo koduojama, 
# arba įsisavinti kodą skaitančiajam
# Komentuoti galima vieną eilutę (“#” pagalba) arba kodo fragmentą
# komentuoti galima tiek prieš kodą, tiek kodo eilutėje
# Per daug komentarų - kas per daug , tas nesveika
# Rekomenduojama teisingiau, aiškiau pavadinti programos komponentus, nei prirašyti per daug komentarų
# https://realpython.com/python-pep8/