# env

> Toon de omgeving of voer een programma uit in een aangepaste omgeving.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html>.

- Toon de environment:

`env`

- Voer een programma uit. Meestal gebruikt in scripts na de shebang (#!) voor het opzoeken van het pad naar het programma:

`env {{programma}}`

- Wis de omgeving en voer een programma uit:

`env {{[-i|--ignore-environment]}} {{programma}}`

- Verwijder een variabele van de omgeving en voer een programma uit:

`env {{[-u|--unset]}} {{variabele}} {{programma}}`

- Zet een variabele en voer een programma uit:

`env {{variabele}}={{waarde}} {{programma}}`

- Zet meerdere variabelen en voer een programma uit:

`env {{variabele1=waarde variabele2=waarde variabele3=waarde ...}} {{programma}}`

- Voer een programma uit onder een andere naam:

`env {{[-a|--argv0]}} {{aangepaste_naam}} {{programma}}`
