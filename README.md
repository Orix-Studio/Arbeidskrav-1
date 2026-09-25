Noah Holmvik

GITHUB REPO:
https://github.com/Orix-Studio/Arbeidskrav-1

Oppgave 1:
NB! Denne oppgaven er løst UTEN bruk av KI

GENERELT:
Her har jeg valgt å holde hovedfilen så enkel og oversiktlig som mulig. Alle funksjoner er lagt i egen fil som importeres og påkalles i hovedfilen.
Programmet kjøres i en while-loop inntil den brytes ved at brukeren velger menyvalget for å avslutte programmet.

MENY:
Tast 1-3 er lenket til hver sin funksjon, og kjøres hvis brukeren taster inn et tall mellom 1-3. Tast 4 bryter while-loopen og avslutter programmet.
Input for menyvalg er låst til å være et tall (int), og derfor benytter jeg try/except for å ta imot erroren og outputte en feilmelding til brukeren hvis de skriver inn noe annet enn et tall. Hvis brukeren derimot skriver inn et tall som ikke matcher noen av menyvalgene, vil de også på en feedback på at menyvalget ikke finnes.

BRUK AV GOOGLE:
Det eneste jeg trengte hjelp til i oppgave 1 var å reversere en string. Dette fant jeg svar på her, via Google søk: [::-1]
https://stackoverflow.com/questions/931092/how-do-i-reverse-a-string-in-python 



Oppgave 2:
NB! Denne oppgaven er løst med MINIMAL bruk av KI

GENERELT:
Denne oppgaven har jeg fokusert på å holde hovedfilen minimalistisk og oversiktlig, samtidig som at hele programmet er dynamisk og enkelt å bygge videre på. Funksjoner er faset ut i en egen fil, og importeres til hovedfilen.

GIT:
Denne oppgaven har små commits hele veien, for hver delvis fullførte bragd i oppgaven. Hver commit har tydelige beskrivelser som er enkle å forstå.

MENY:
Menyinnholdet er lagt inn i en liste. Hver list item har en beskrivende tekst og en funksjon tilknyttet seg. 
Menyen printes ut til brukeren ved bruk av en for-loop. For-loopen er brukt sammen med enumerate med start=1. Dette gjør at hver item i for-loopen får en index som starter fra 1. Første item får index 1, andre item får 2 osv.
Denne indexen brukes til å gi menyvalget et tall som vist under:
1. Menyvalg #1
2. Menyvalg #2
3. Menyvalg #3

Brukeren blir deretter spurt om menyvalg, og her må de velge et tall mellom 1 og len(menu), ellers får de en feilmelding om at menyvalget ikke finnes. Try/except er også brukt her for å ikke kræsje programmet hvis brukeren oppgir noe annet enn et tall.
Hvis brukeren taster inn '1', så forteller programmet at den skal starte funksjonen til første item i menu-listen. Da må programmet finne menu item med index som tilsvarer den første. Siden index starter på 0 og ikke én, må vi kalle på item[1 - 1].
Det samme gjelder for menypunkt 5. Menypunkt 5 har index item[5 - 1], altså index 4.

AVSLUTTE PROGRAM:
Menyen og programmet kjører helt til programmet avsluttes ved å kjøre en funksjon som returnerer False. Jeg har laget en if-setning i while-loopen som holder programmet kjørende som sier at hvis funksjonen returnerer False, så skal while-loopen settes til False.

FUNKSJONER:
Alle funksjoner er faset ut i egen fil og importeres til hovedfilen. Alle funksjoner kjøres med et parameter random_function(sessions). sessions er listen med alle økter som er registrert med data for hver økt. Funksjonene trenger denne listen med data for å kunne utføre handlingene sine, og den må derfor føres inn i funksjonen på et vis.
Funksjoner er også testet lokalt i FunctionsLibrary.py filen ved bruk av:
if __name__ == "__main__":

EKSTRA TANKER:
Funksjonen for å avslutte programmet kunne også hatt en funksjon hvor den lagrer listen sessions = [...] i en ekstern fil, men dette tok jeg ikke med ettersom det ikke var et krav til oppgaven. Eventuelt kunne den også lagret for hver loop i programmet, eller hver gang sessions listen endrer seg.

BRUK AV KI:
Jeg brukte KI for å kunne sortere listen med økter utifra varigheten på økten item["duration"]. Jeg forsøkte først å legge hver item i en ny liste slik som nye items med varigheten som key [item"duration", item_data]:
[90: {...data}, 40: {...data}, 20: {...data}, 120: {...data}]

Deretter prøvde jeg å .sort(reverse=True), men programmet kræsjet hvis det var to økter med lik varighet.

Jeg spurte deretter KI om hvordan jeg kunne sortere items i en liste utifra dataen "duration" i hver item. Da fikk jeg denne løsningen som bruker:
sorted_sessions_list = sorted(session_list, key=lambda item: item["duration"], reverse=True)

Denne linjen bruker sorted isteden for .sort(). Hovedforskjellen er at .sort() sorterer en allerede eksisterende liste, mens sorted lager en ny liste med dataene fra listen man oppgir.
Denne linjen fra KI gir meg en ny liste der key blir satt til gjeldende varighet for økten, for hver økt i listen. Deretter sorteres den ved hjelp av key på hver item, baklengs ettersom reverse=True. Da blir resultatet en ny liste der hver økt er sortert fra lengst til kortest varighet.



Oppgave 3:
NB! Denne oppgaven er løst med MINIMAL bruk av KI

DATETIME FUNKSJONER BENYTTET FRA PYTHON DOCS: 
datetime.date() - opprette og validere datoer
datetime.time() - opprette og validere tidspunkter
datetime.combine() - kombinere date og time for å få en datetime-verdi
timedelta() - Gjøre timer og minutter mulig å kombinere med en datetime for å finne en slutt-tid for økten (Startdato og tidspunkt + antall timer og minutter)
strftime() - Gjøre datetime-verdi om til menneskelig format, f.eks. (Monday, 15. December 2026)
https://docs.python.org/3/library/datetime.html

Bruk av KI:
Jeg brukte KI for å sortere dictionariet med forskjellige klasser. Jeg spurte KI om følgende:
"Hvordan sorterer jeg en dictionary med klasser i dette formatet":
class_list {
   2025-12-24 10:00:00: {
      "start": 2025-12-24 10:00:00,
      "hours": 1,
      "minutes": 0,
      "end": 2025-12-24 11:00:00,
   }
   2025-12-25 10:00:00: {
      "start": 2025-12-25 10:00:00,
      "hours": 1,
      "minutes": 0,
      "end": 2025-12-25 11:00:00,
   }
}

Da fikk jeg denne linjen til svar:
sorted_class_list = {key: class_list[key] for key in sorted(class_list)}

Det denne linjen med kode gjør er at den oppretter et nytt dictionary for listen. Det nye dictionariet sorterer hver item, og bruker datetime som key for å sortere. 
Det eneste problemet her er at det ikke var mulig å ha flere klasser med samme start-tid, for da ble også key for disse identiske.

Løsningen jeg kom opp med var å endre hele class_list til en liste [], i steden for et dictionary {}.
Deretter endret jeg sorteringen til å sortere gjennom item['start'] inni hver enkel item.
sorted_class_list = sorted(class_list, key=lambda item: item['start'])

TESTTILFELLER:

TEST 1 - OPPRETTING AV STUDIEØKT:
Input:
Startdato: 15.10.2005
Starttid: 10:00
Varighet (m): 60

Output:
The class starts Thursday, 15. October 2026 at 10:00.
The class ends Thursday, 15. October 2026 at 11:00.
The class lasts 1 hour and 00 minutes.


TEST 2 - STUDIEØKT OVER MIDNATT:
Input:
Startdato: 22.9.2026
Starttid: 23:30
Varighet (m): 90

Output:
The class starts Tuesday, 22. September 2026 at 23:30.
The class ends Wednesday, 23. September 2026 at 01:00.
The class lasts 1 hour and 30 minutes.


TEST 3 - FEIL DATOFORMAT:
Input:
Startdato: 2026-10-15

Output:
Date format is submitted wrong. Try again.


TEST 4 - UGYLDIG DATO:
Input:
Startdato: 31.2.2026

Output:
Date is not valid. Try again.


TEST 5 - UGYLDIG KLOKKESLETT:
Input:
Starttid: 25:00

Output:
Time is not valid. Try again.


TEST 6 - VARIGHET OPPGITT SOM STRING:
Input:
Varighet: Twenty

Output:
Time is not valid. Try again.


TEST 7 - VARIGHET SATT TIL 0 MINUTTER:
Input:
Varighet: 0

Output:
Length cannot be 0 or below.


TEST 8 - DATOER OPPGIS I FEIL REKKEFØLGE, VED KALKULERING AV ANTALL DAGER MELLOM 2 DATOER:
Input:
Første dato: 20.9.2026
Andre dato: 15.9.2026

Output:
There is 5 days between the two dates. (This is because I use abs() around the calculation. -5 therefore shows as 5)


TEST 9 - SORTERING AV STUDIEØKTER:
Første registrerte studieøkt: 15.10.2026 10:00
Andre registrerte studieøkt: 10.10.2026 10:00

Output:
1. class:
Start: 2026-10-10 10:00:00
End: 2026-10-10 11:00:00
Duration: 1 hours and 0 minutes

2. class:
Start: 2026-10-15 10:00:00
End: 2026-10-15 11:00:00
Duration: 1 hours and 0 minutes



Oppgave 4.1:
Ingen bruk av KI, kun leksjonen "Python 8- Wednesday: File Handling (File I/O)" i MinGA.


Oppgave 4.2:
Brukte Google for å finne ut hvordan jeg kunne korte float ned til én desimal.
Kilde: https://www.geeksforgeeks.org/python/how-to-round-floating-value-to-two-decimals-in-python/


Oppgave 4.3:
Ingen bruk av KI.
Oppgaven er merget med 4.2 for å unngå duplikate handlinger og prosesser.

Ugyldige rader vises allerede i terminalen fra Oppgave 4.1, og er ikke med i analysen eller rapporten.


Oppgave 4.4:
Jeg fant og fikset 4 feil som gjør at funksjonen nå fungerer:

1. "str | int" støttes ikke av Python 3.9, og må endres til Union[str, int] (Pycharm ga tilsvarende feilmelding).
2. Endre = med == som er riktig syntax for å matche verdier.
3. Endre = til += for å addere totalen med gjeldende minutter, og ikke erstatte total med gjeldende minutter.
4. Returnere total, isteden for total_minutes, ettersom total_minutes ikke finnes og har ingen verdi å returnere.

Jeg har kommentert per linje i oppgave-4.py, der jeg har rettet opp en feil. Jeg har også testet funksjonen og sett at den fungerer med fiktive data.



Oppgave 5:
INGEN bruk av KI for denne oppgaven

Dokumentasjon brukt for bruk av klasse:
Min GA: Python10-Wednesday: Classes, Objects & Assignment Preparation