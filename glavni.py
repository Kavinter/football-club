import Zaposleni
import Statistika
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import pandas as pd

def main():
    print()
    print("Fudbalski Klub Fajenord Roterdam")
    print("********************************")
    print()
    mt = login()
    if mt == False:
        print("\nNiste uneli postojece korisnicko ime ili lozinku.")
        return 
    komanda = '0'
    if mt.upper() == 'T':
        while komanda != 'X':
            komanda = menu(mt)
            if komanda == '1':
                traziigraca()
            elif komanda == '2':
                listaigraca()
            elif komanda == '3':
                statistikasvihigraca()
            elif komanda == '4':
                statistikaigraca()
            elif komanda == '5':
                infoklub()
            elif komanda == '6':
                xgstatistika()
            elif komanda == '7':
                listamenadzera()
                
    elif(mt == 'M'):
        while komanda != 'X':
            komanda = menu(mt)
            if komanda == '1':
                traziigraca()
            elif komanda == '2':
                listaigraca()
            elif komanda == '3':
                statistikasvihigraca()
            elif komanda == '4':
                statistikaigraca()
            elif komanda == '5':
                infoklub()
            elif komanda == '6':
                xgstatistika()
            elif komanda == '7':
                listatrenera()
            elif komanda == '8':
                dodajtrenera()
            elif komanda == '9':
                izmenitrenera()
            elif komanda == '10':
                obrisitrenera()
            elif komanda == '11':
                dodajigraca()
                
    print("Dovidjenja.")

def login():
    mentre = input("Unesite \"m\" ako ste menadzer, a \"t\" ako ste trener: ")
    username = input("Unesite korisnicko ime: ")
    password = input("Unesite lozinku: ")
    if mentre.upper() == 'M':
        return Zaposleni.loginmenadzer(username, password)
    elif mentre.upper() == 'T':
        return Zaposleni.logintrener(username, password)
    else:
        return False

def menu(mt):
    komandemenadzer = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 'X']
    komandetreneri = ['1', '2', '3', '4', '5', '6', '7', 'X']
    printMenu(mt)
    komanda = input(">> ")
    if mt.upper() == 'M':
        while komanda.upper() not in komandemenadzer:
            print("\nUneli ste pogresnu komandu.\n")
            printMenu(mt)
            komanda = input(">> ")
    elif mt.upper() == 'T':
        while komanda.upper() not in komandetreneri:
            print("\nUneli ste pogresnu komandu.\n")
            printMenu(mt)
            komanda = input(">> ")
    return komanda.upper()



def printMenu(mt):
    if(mt == 'T'):
        print("\nIzaberite komandu:")
        print(" 1 - Trazi igraca")
        print(" 2 - Lista igraca")
        print(" 3 - Statistika svih igraca")
        print(" 4 - Statistika posebnog igraca")
        print(" 5 - Informacije o klubu")
        print(" 6 - xG statistika")
        print(" 7 - Lista menadzera")
        print(" X - Izlaz iz programa")
    elif(mt == 'M'):
        print("\nIzaberite komandu:")
        print(" 1 - Trazi igraca")
        print(" 2 - Lista igraca")
        print(" 3 - Statistika svih igraca")
        print(" 4 - Statistika posebnog igraca")
        print(" 5 - Informacije o klubu")
        print(" 6 - xG statistika")
        print(" 7 - Lista trenera")
        print(" 8 - Dodaj trenera")
        print(" 9 - Izmeni trenera")
        print(" 10 - Obrisi trenera")
        print(" 11 - Dodaj igraca")
        print(" X - Izlaz iz programa")
        
#Komande trenera i menadzera
def traziigraca():
    print("1) Trazi igraca")
    naziv = input("Unesite korisnicko ime igraca: ")
    ziv = Zaposleni.pronadjiigraca(naziv)
    if ziv != None:
        print(Zaposleni.igraciheader())
        print(Zaposleni.igracformat(ziv))
    else:
        print("Igrac cije korisnicko ime ste uneli se ne nalazi u sistemu.")

def listaigraca():
    print("2) Lista igraca")
    print(Zaposleni.igraciheader())
    print(Zaposleni.igraciformat())

def statistikasvihigraca():
    print("3) Statistika svih igraca")
    Statistika.izracunaj_prosecnu_ocenu_svih_igraca()
    Statistika.izracunaj_ukupno_golova_svih_igraca()
    Statistika.izracunaj_ukupno_asistencija_svih_igraca()
    Statistika.izracunaj_ukupno_cleansheetova_svih_igraca()
    print(Statistika.statistikaheader())
    with open('statistika.txt', 'r') as f:
        for line in f:
            pod = line.strip().split('|')
            sta = {
                'prosecnaocena': pod[0],
                'golovi': pod[1],
                'asistencije': pod[2],
                'cleansheet': pod[3],
                'username': pod[4]
            }
            print(Statistika.statistikaformat(sta))
    
def statistikaigraca():
    print("4) Statistika odabranog igraca")
    Statistika.izracunaj_prosecnu_ocenu_svih_igraca()
    Statistika.izracunaj_ukupno_golova_svih_igraca()
    Statistika.izracunaj_ukupno_asistencija_svih_igraca()
    Statistika.izracunaj_ukupno_cleansheetova_svih_igraca()
    ime_igraca = input("Unesite korisnicko ime igraca: ")
    with open('statistika.txt', 'r') as f:
        for line in f:
            pod = line.strip().split('|')
            if pod[4] == ime_igraca:
                sta = {
                    'prosecnaocena': pod[0],
                    'golovi': pod[1],
                    'asistencije': pod[2],
                    'cleansheet': pod[3],
                    'username': pod[4]
                }
                print(Statistika.statistikaheader())
                print(Statistika.statistikaformat(sta))
                return
    print('Igrac sa tim imenom nije pronađen')

def infoklub():
    table = PrettyTable()
    table.field_names = ["5) Informacije o klubu"]
    table.add_row(["Fajenord Roterdam je profesionalni klub iz holandskog grada Roterdama. Osnovan je 19. jula 1908. godine i trenutno se takmiči u Erediviziji (najveci rang holandskog takmicenja)."])
    table.add_row(["Fajenord je jedan od najvecih fudbalskih klubova u Holandiji, klub je osvojio: "])
    table.add_row(["15 titula prvaka Holandije \n 13 trofeja kupa Holandije \n 4 superkupa Holandije"])
    table.add_row(["Dok od medjunarodnih trofeja ima:"])
    table.add_row(["1 kup evropskih sampiona \n 2 kupa UEFA \n 1 trofej interkontinentalnog kupa"])
    table.add_row(["Svoje domace utakmice igra na stadionu Fajenorda, poznatijem po nadimku „De Kujp” (korito), koji ima kapacitet od preko 51.000 sedecih mesta."])
    print(table)
    
def xgstatistika():
    print("6) xG statistika")
    df = pd.read_csv('xgll.csv')

    a_xG=[0]
    h_xG=[0]
    a_min=[0]
    h_min=[0]

    #nadji domaci ili gostujuci klub
    hteam=df['h_a'].iloc[0]
    ateam=df['h_a'].iloc[-1]

    for x in range(len(df['xG'])):
        if df['h_a'][x]==ateam:
            a_xG.append(df['xG'][x])
            a_min.append(df['minute'][x])
        if df['h_a'][x]==hteam:
            h_xG.append(df['xG'][x])
            h_min.append(df['minute'][x])

    def sabirakxgliste(lista):
        return [sum(lista[:i+1]) for i in range(len(lista))]

    a_sabirak=sabirakxgliste(a_xG)
    h_sabirak=sabirakxgliste(h_xG)


    fig, ax = plt.subplots(figsize=(10,5))
    fig.set_facecolor('#3d4849')
    ax.patch.set_facecolor('#3d4849')

    plt.xticks([0,15,30,45,60,75,90])

    plt.title('xG grafik sa poslednje utakmice')
    plt.xlabel('Minuta')
    plt.ylabel('XG')

    ax.step(x=a_min,y=a_sabirak,where='post')
    ax.step(x=h_min,y=h_sabirak,where='post')
    
    plt.show()
    
#Komande trenera

def listamenadzera():
    print("7) Lista menadzera")
    print(Zaposleni.menadzerheader())
    print(Zaposleni.menadzeriformat())
    
#Komande menadzera 
def listatrenera():
    print("7) Lista trenera")
    print(Zaposleni.treneriheader())
    print(Zaposleni.treneriformat())
    
def dodajtrenera():
    print("8) Dodaj trenera")
    ime = input("\nUnesite ime trenera: ")
    prezime = input("Unesite prezime trenera: ")
    vrsta = input("Unesite kojom vrstom treninga se bavi trener: ")
    username = input("Unesite korisnicko ime trenera: ")
    while Zaposleni.pronadjitrenera(username) != None:
        print("To korisnicko ime je vec zauzeto.")
        username = input("Unesite korisnicko ime trenera: ")
    password = input("Unesite lozinku trenera: ")
    tre={'ime':ime, 'prezime':prezime, 'vrsta':vrsta, 'username':username, 'password':password}
    Zaposleni.dodajtrenera(tre)
    Zaposleni.savetreneri()
    
def izmenitrenera():
    print("9) Izmeni trenera")
    naziv = input("\nUnesite korisnicko ime trenera cije podatke zelite izmeniti: ")
    tre = Zaposleni.pronadjitrenera(naziv)
    if tre != None:
        izmena = '0'
        while izmena.upper() != 'X':
            print("Koji podatak zelite izmeniti?")
            print("1 - Ime trenera")
            print("2 - Prezime trenera")
            print("3 - Vrstu treninga trenera")
            print("4 - Korisnicko ime trenera")
            print("5 - Lozinku trenera")
            print("X - Izlaz iz izmene trenera")
            izmena = input("\n>>")
            
            while izmena.upper() not in ('1', '2', '3', '4', '5', 'X'):
                print("Niste uneli postojecu komandu. Unesite komandu: ")
                izmena = input(">>")
                
            if izmena == '1':
                tre['ime'] = input("Unesite novo ime trenera: ")
            elif izmena == '2':
                tre['prezime'] = input("Unesite novo prezime trenera: ")
            elif izmena == '3':
                tre['vrsta'] = input("Unesite novu vrstu treninga koji trener pruza: ")
            elif izmena == '4':
                tre['username'] = input("Unesite novo korisnicko ime trenera: ")
            elif izmena == '5':
                tre['password'] = input("Unesite novu lozinku trenera: ")
            
            Zaposleni.savetreneri()
    else:
        print("Trener cije ste korisnicko ime uneli ne postoji.")
        
def obrisitrenera():
    print("10) Obrisi trenera")
    naziv = input("\nUnesite korisnicko ime trenera kojeg zelite obrisati: ")
    tre = Zaposleni.pronadjitrenera(naziv)
    if tre != None:
        Zaposleni.obrisitrenera(tre)
        Zaposleni.savetreneri()
        print("Uspesno ste obrisali odabranog trenera!")
    else:
        print("Trener cije ste korisnicko ime uneli ne postoji.")
        
def dodajigraca():
    print("11) Dodaj igraca")
    ime = input("\nUnesite ime igraca: ")
    prezime = input("Unesite prezime igraca: ")
    pozicija = input("Unesite poziciju igraca: ")
    nacionalnost = input("Unesite nacionalnost igraca: ")
    godine = input("Unesite koliko godina ima igrac: ")
    visina = input("Unesite visinu igraca (unesite cm na kraju): ")
    tezina = input("Unesite tezinu igraca (unesite kg na kraju): ")
    username = input("Unesite korisnicko ime igraca: ")
    while Zaposleni.pronadjiigraca(username) != None:
        print("To korisnicko ime je vec zauzeto.")
        username = input("Unesite korisnicko ime igraca: ")
    igr={'ime':ime, 'prezime':prezime, 'pozicija':pozicija, 'nacionalnost':nacionalnost, 'godine':godine, 'visina':visina, 'tezina':tezina, 'username':username}
    Zaposleni.dodajigraca(igr)
    Zaposleni.saveigraci()
    

print(__name__)
if __name__ == '__main__':
    main()