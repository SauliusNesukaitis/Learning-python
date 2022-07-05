# 4. Polimorfizmas (Polymorphism) – galimybė operacijas (metodus) vykdyti skirtingai, 
# priklausomai nuo konkrečios klasės (ar duomenų tipo) realizacijos,
# metodo kvietėjui nežinant apie tuos skirtumus. 
# Tai pasiekiama perrašant tam tikrus metodus vaikinėse klasėse.

# Galima skirti tokius polimorfizmo tipus: 
# operatorių užklojimas,
# metodų užklojimas,
# abstrakčiųjų metodų naudojimas.

# Statinis polimorfizmas
# Operatorių ir metodų užklojimas – tai statinis polimorfizmas.
# Kokią prasmę suteikti operatoriui ar metodui, programą kompiliuojanti ir vykdanti sistema nusprendžia kompiliavimo metu (angl. compile time).

# Dinaminis polimorfizmas
# Polimorfizmas leidžia visą klasių šeimą, turinčią vieną bazinę klasę, apdoroti lyg visi objektai būtų bazinės klasės objektai.
# Tokią klasių šeimą lengva plėsti, papildant naujomis klasėmis, nes nereikia rūpintis naująja klase.
# Virtualūs bazinės ir išvestinių klasių metodai bei bazinės klasės objektų nuorodos sudaro dinaminį polimorfizmą.
# Kurį metodą (bazinės ar išvestinės klasės) vykdyti, programą kompiliuojanti ir vykdanti sistema nusprendžia programos vykdymo metu (angl. run time). Tai vadinama dinaminiu susietumu arba užvėlintu susiejimu.
# Dažnai dinaminis polimorfizmas vadinamas tiesiog polimorfizmu.


# Metodo (funkcijos) perrašymas (Overriding):

class Gyvunas():
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva
    
    def begti(self):
        print("Begu")

class Vezlys(Gyvunas):
    def begti(self):
        super().begti() # pasiekiame tevines klases metoda per super().metodas()
        print("As einu letai")


gyvunas = Gyvunas("Rokis", "juodas")
gyvunas.begti()

vezlys = Vezlys("Tadas","Rudas")
vezlys.begti()


# Kaip pasiekti tėvinės klasės metodą:

#super().begti() # pasiekiame tevines klases metoda per super().metodas()

# Kaip vaikinei klasei pridėti papildomas savybes:
class Tevas: 
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde 

class Vaikas(Tevas):
    def __init__(self, vardas, pavarde, mokymosi_istaiga):
        super().__init__(vardas, pavarde) # paveldimas konstruktorius tevines klases
        self.mokymosi_istaiga = mokymosi_istaiga

tevas = Tevas("Gintautas", "Paskauskas")
vaikas = Vaikas("Gintare", "Laucienė", "Kauno technolpgijos universitetas")

#print(tevas.mokymosi_istaiga()) #AttributeError: 'Tevas' object has no attribute 'mokymosi_istaiga'

print(vaikas.mokymosi_istaiga)

# Kaip patikrinti, kokiai klasei priklauso objektas (biudžeto pavyzdys):
class Irasas:
    def __init__(self, suma):
        self.suma

class PajamuIrasas(Irasas):
    pass

class IslaiduIrasas(Irasas):
    pass

biudzetas = []

