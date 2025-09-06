# cal

> Toon een kalender met de huidige dag gemarkeerd.
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Toon een kalender voor de huidige maand:

`cal`

- Toon een kalender voor een specifiek jaar:

`cal {{jaar}}`

- Toon een kalender voor een specifieke maand en jaar:

`cal {{maand}} {{jaar}}`

- Toon de volledige kalender voor het huidige jaar:

`cal -y`

- Markeer ([h]) vandaag niet en toon [3] maanden rondom de datum:

`cal -h -3 {{maand}} {{jaar}}`

- Toon de 2 maanden voor ([B]) en 3 maanden na ([A]) een specifieke [m]aand van het huidige jaar:

`cal -A 3 -B 2 {{maand}}`

- Toon [j]ulian dagen (beginnend vanaf één, genummerd vanaf 1 januari):

`cal -j`
