Noah Holmvik


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
