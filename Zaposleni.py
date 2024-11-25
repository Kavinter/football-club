
#funkcionalnosti zaposlenih (menadzer i treneri) u fudbalskom klubu. 
#igraci su zaposleni ali nemaju pravo na ulazak u program.
#menadzeri, treneri i igraci se ucitavaju iz fajlova u recnik
#kljucevi u recniku su ime, prezime, korisnicko ime i lozinka za menadzera.
#kljucevi u recniku su ime, prezime, vrsta, korisnicko ime i lozinka za trenera.
#kljucevi u recniku za igrace su: ime, prezime, pozicija, nacionalnost, godine, visina, tezina i korisnicko ime.

#login menadzera
def loginmenadzer(username, password):
    for m in menadzer:
        if m['username']==username and m['password']==password:
            return 'M'
    return False

#login trenera
def logintrener(username, password):
    for t in treneri:
        if t['username']==username and t['password']==password:
            return 'T'
    return False

#ucitavanje trenera u recnik
def ucitajtrenere():
    for l in open ('treneri.txt','r'):
        tre=str2tre(l)
        treneri.append(tre)

#ucitavanje menadzera u recnik
def ucitajmenadzera():
    for l in open ('menadzer.txt','r'):
        men=str2men(l)
        menadzer.append(men)

#ucitavanje igraca u recnik
def ucitajigrace():
    for l in open ('igraci.txt','r'):
        igr=str2igr(l)
        igraci.append(igr)

def str2tre(line):
    line = line.strip() 
    ime, prezime, vrsta, username, password = line.split('|')
    tre = {'ime': ime,
           'prezime': prezime,
           'vrsta': vrsta,
           'username': username,
           'password': password}
    return tre


def str2men(line):
    line = line.strip()
    ime, prezime, username, password = line.split('|')
    men = {'ime': ime,
           'prezime': prezime,
           'username': username,
           'password': password}
    return men

def str2igr(line):
    if line[-1] =='\n':
        line = line[:-1]
    ime,prezime,pozicija,nacionalnost,godine,visina,tezina,username=line[:-1].split('|')
    igr={'ime': ime,
         'prezime': prezime,
         'pozicija': pozicija,
         'nacionalnost': nacionalnost,
         'godine': godine,
         'visina': visina,
         'tezina': tezina,
         'username': username}
    return igr

def men2str(men):
    return '|'.join([men['ime'],men['prezime'],men['username'],men['password']])

def tre2str(tre):
    return '|'.join([tre['ime'],tre['prezime'],tre['vrsta'],tre['username'],tre['password']])

def igr2str(igr):
    return '|'.join([igr['ime'],igr['prezime'],igr['pozicija'],igr['nacionalnost'],igr['godine'],igr['visina'],igr['tezina'],igr['username']])

def svitreneri():
    return treneri

def sviigraci():
    return igraci

def dodajtrenera(tre):
    treneri.append(tre)

def dodajigraca(igr):
    igraci.append(igr)

#pronalazi menadzera po korisnickom imenu
def pronadjimenadzera(username):
    for m in menadzer:
        if m['username'] == username:
            return m
    return None

#pronalazi trenera po korisnickom imenu
def pronadjitrenera(username):
    for r in treneri:
        if r['username'] == username:
            return r
    return None

#pronalazi igraca po korisnickom imenu
def pronadjiigraca(username):
    for i in igraci:
        if i['username'] == username:
            return i
    return None

#formatira header za ispis menadzera
def menadzerheader():
    return \
        "Ime       |Prezime        \n"\
        "----------+---------------"

#formatira header za ispis trenera
def treneriheader():
    return \
        "Ime       |Prezime        |Vrsta          |Username  |Lozinka   \n"\
        "----------+---------------+---------------+----------+----------"

#formatira header za ispis igraca
def igraciheader():
    return \
        "Ime       |Prezime        |Pozicija       |Nacionalnost   |Godine    |Visina    |Tezina    |Username  \n"\
        "----------+---------------+---------------+---------------+----------+----------+----------+----------"

#formatira ispis menadzera koji je prosledjen
def menadzerformat(men):
    return u"{0:10}|{1:15}".format(men['ime'], men['prezime'])

#formatira ispis trenera koji je prosledjen
def trenerformat(tre):
    return u"{0:10}|{1:15}|{2:15}|{3:10}|{4:10}".format(tre['ime'], tre['prezime'], tre['vrsta'], tre['username'], tre['password'])

#formatira ispis igraca koji je prosledjen
def igracformat(igr):
    return u"{0:10}|{1:15}|{2:15}|{3:15}|{4:10}|{5:10}|{6:10}|{7:10}".format(igr['ime'],igr['prezime'],igr['pozicija'],igr['nacionalnost'],igr['godine'],igr['visina'],igr['tezina'],igr['username'])

#formatira ispis svih menadzera u recniku menadzer
def menadzeriformat():
    rez = ""
    for men in menadzer:
        rez += menadzerformat(men) + '\n'
    return rez

#formatira ispis svih trenera u recniku treneri
def treneriformat():
    rez = ""
    for tre in treneri:
        rez += trenerformat(tre) + '\n'
    return rez

#formatira ispis svih igraca u recniku igraci
def igraciformat():
    rez = ""
    for igr in igraci:
        rez += igracformat(igr) + '\n'
    return rez

#iz recnika treneri, funkcija brise prosledjenog trenera
def obrisitrenera(tre):
    treneri.remove(tre)

#igraci se ne brisu jer su pod ugovorom do kraja sezone
#menadzera moze samo predsednik kluba da obrise

def savetreneri():
    fajl = open('treneri.txt', 'w')
    for t in treneri:
        fajl.write(tre2str(t))
        fajl.write('\n')
    fajl.close()

def saveigraci():
    fajl = open('igraci.txt', 'w')
    for i in igraci:
        fajl.write(igr2str(i))
        fajl.write('\n')
    fajl.close()


print(__name__)      
menadzer = []
treneri= []
igraci= []
ucitajmenadzera()
ucitajtrenere()
ucitajigrace()

