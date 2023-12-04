# env

> Toon de omgeving of voer een programma uit in een aangepaste omgeving.
> Meer informatie: <https://www.gnu.org/software/coreutils/env>.

- Toon de environment:

`env`

- Voer een programma uit. Meestal gebruikt in scripts na de shebang (#!) voor het opzoeken van het pad naar het programma:

`env {{programma}}`

- Wis de omgeving en voer een programma uit:

`env -i {{programma}}`

- Verwijder een variable van de omgeving en voer een programma uit:

`env -u {{variable}} {{programma}}`

- Zet een variable en voer een programma uit:

`env {{variable}}={{waarde}} {{programma}}`

- Zet meerdere variablen en voer een programma uit:

`env {{variable1}}={{waarde}} {{variable2}}={{waarde}} {{variable3}}={{waarde}} {{programma}}`
