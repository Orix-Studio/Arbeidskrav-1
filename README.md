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