# cal

> Toon een kalender.
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Toon een kalender voor de huidige maand:

`cal`

- Toon een kalender voor een specifiek jaar:

`cal {{jaar}}`

- Toon een kalender voor een specifieke maand en jaar:

`cal {{maand}} {{jaar}}`

- Toon de volledige kalender voor het huidige jaar door gebruik te maken van [j]ulian dagen  (beginnend vanaf één, genummerd vanaf 1 januari):

`cal -y -j`

- Markeer ([h]) vandaag en toon [3] maanden rondom de datum::

`cal -h -3 {{maand}} {{jaar}}`

- Toon de 2 maanden voor ([B]) en 3 maanden na ([A]) een specifieke [m]aand van het huidige jaar:

`cal -A 3 -B 2 {{maand}}`

- Toon een specifiek aantal maanden voor en na (Context) de opgegeven maand:

`cal -C {{maanden}} {{maand}}`

- Specificeer de startdag van de week (0: Zondag, 1: Maandag, ..., 6: Zaterdag):

`cal -d {{0..6}}`
