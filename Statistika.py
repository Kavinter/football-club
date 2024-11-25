#formatira header za ispis statistike igraca
def statistikaheader():
    return \
        "Prosek    |Golovi         |Asistencije    |Cleansheet |Username   \n"\
        "----------+---------------+---------------+-----------+----------"

#formatira ispis statistike koja je prosledjena
def statistikaformat(sta):
    return u"{0:10}|{1:15}|{2:15}|{3:11}|{4:10}".format(sta['prosecnaocena'], sta['golovi'], sta['asistencije'], sta['cleansheet'], sta['username'])

#Ispisuje prosecnu ocenu svih igraca sa poslednjih 10 utakmica i upisuje je u statistika.txt fajl
def izracunaj_prosecnu_ocenu_svih_igraca():
    igraci_info = {}
    with open("igraci.txt", "r") as f:
        for line in f:
            parts = line.strip().split("|")
            ime, prezime, pozicija, zemlja, godine, visina, tezina, korisnicko_ime_read = parts
            igraci_info[korisnicko_ime_read] = ime, prezime, pozicija, zemlja, godine, visina, tezina

    with open("ocene.txt", "r") as f:
        ocene = {}
        for line in f:
            parts = line.strip().split("|")
            korisnicko_ime_read = parts[0]
            ratings = [float(x) for x in parts[1:]]
            ocene[korisnicko_ime_read] = ratings

    with open("statistika.txt", "r") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        parts = lines[i].strip().split("|")
        korisnicko_ime_read = parts[-1]
        if korisnicko_ime_read in ocene:
            ocena = round(sum(ocene[korisnicko_ime_read][-10:])/10, 2)
            ime, prezime, pozicija, zemlja, godine, visina, tezina = igraci_info[korisnicko_ime_read]
            lines[i] = f"{ocena}|{parts[1]}|{parts[2]}|{parts[3]}|{korisnicko_ime_read}\n"
    
    with open("statistika.txt", "w") as f:
        f.writelines(lines)

#Ispisuje ukupan broj golova svih igraca i upisuje u statistika.txt fajl
def izracunaj_ukupno_golova_svih_igraca():
    igraci_info = {}
    with open("igraci.txt", "r") as f:
        for line in f:
            parts = line.strip().split("|")
            ime, prezime, pozicija, zemlja, godine, visina, tezina, korisnicko_ime_read = parts
            igraci_info[korisnicko_ime_read] = ime, prezime, pozicija, zemlja, godine, visina, tezina

    with open("golovi.txt", "r") as f:
        golovi = {}
        for line in f:
            parts = line.strip().split("|")
            korisnicko_ime_read = parts[0]
            goals = [int(x) for x in parts[1:] if x]
            golovi[korisnicko_ime_read] = goals

    with open("statistika.txt", "r") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        parts = lines[i].strip().split("|")
        korisnicko_ime_read = parts[-1]
        if korisnicko_ime_read in golovi:
            ukupno_golova = sum(golovi[korisnicko_ime_read])
            ime, prezime, pozicija, zemlja, godine, visina, tezina = igraci_info[korisnicko_ime_read]
            lines[i] = f"{parts[0]}|{ukupno_golova}|{parts[2]}|{parts[3]}|{korisnicko_ime_read}\n"

    with open("statistika.txt", "w") as f:
        f.writelines(lines)
   
#Ispisuje ukupan broj asistencija svih igraca i upisuje u statistika.txt fajl
def izracunaj_ukupno_asistencija_svih_igraca():
    igraci_info = {}
    with open("igraci.txt", "r") as f:
        for line in f:
            parts = line.strip().split("|")
            ime, prezime, pozicija, zemlja, godine, visina, tezina, korisnicko_ime_read = parts
            igraci_info[korisnicko_ime_read] = ime, prezime, pozicija, zemlja, godine, visina, tezina

    with open("asistencije.txt", "r") as f:
        asistencije = {}
        for line in f:
            parts = line.strip().split("|")
            korisnicko_ime_read = parts[0]
            assists = [int(x) for x in parts[1:] if x]
            asistencije[korisnicko_ime_read] = assists

    with open("statistika.txt", "r") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        parts = lines[i].strip().split("|")
        korisnicko_ime_read = parts[-1]
        if korisnicko_ime_read in asistencije:
            ukupno_asistencija = sum(asistencije[korisnicko_ime_read])
            ime, prezime, pozicija, zemlja, godine, visina, tezina = igraci_info[korisnicko_ime_read]
            lines[i] = f"{parts[0]}|{parts[1]}|{ukupno_asistencija}|{parts[3]}|{korisnicko_ime_read}\n"

    with open("statistika.txt", "w") as f:
        f.writelines(lines)

#Ispisuje ukupan broj cleansheetova svih igraca i upisuje u statistika.txt fajl
def izracunaj_ukupno_cleansheetova_svih_igraca():
    igraci_info = {}
    with open("igraci.txt", "r") as f:
        for line in f:
            parts = line.strip().split("|")
            ime, prezime, pozicija, zemlja, godine, visina, tezina, korisnicko_ime_read = parts
            igraci_info[korisnicko_ime_read] = ime, prezime, pozicija, zemlja, godine, visina, tezina

    with open("cleansheet.txt", "r") as f:
        cleansheet = {}
        for line in f:
            parts = line.strip().split("|")
            korisnicko_ime_read = parts[0]
            cleansheets = [int(x) for x in parts[1:] if x]
            cleansheet[korisnicko_ime_read] = cleansheets

    with open("statistika.txt", "r") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        parts = lines[i].strip().split("|")
        korisnicko_ime_read = parts[-1]
        if korisnicko_ime_read in cleansheet:
            ukupno_cleansheet = sum(cleansheet[korisnicko_ime_read])
            ime, prezime, pozicija, zemlja, godine, visina, tezina = igraci_info[korisnicko_ime_read]
            lines[i] = f"{parts[0]}|{parts[1]}|{parts[2]}|{ukupno_cleansheet}|{korisnicko_ime_read}\n"

    with open("statistika.txt", "w") as f:
        f.writelines(lines)



print (__name__)
izracunaj_prosecnu_ocenu_svih_igraca()
izracunaj_ukupno_golova_svih_igraca()
izracunaj_ukupno_asistencija_svih_igraca()
izracunaj_ukupno_cleansheetova_svih_igraca()
statistika = []
ocene= []
igraci = []