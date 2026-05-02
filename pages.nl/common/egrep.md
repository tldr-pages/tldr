# egrep

> Zoek naar patronen in bestanden met behulp van uitgebreide `regex`en.
> Opmerking: dit commando is een alias van `grep --extended-regexp`.
> Meer informatie: <https://manned.org/egrep>.

- Zoek naar één of meer herhaalde tekens:

`egrep '{{a}}+' {{pad/naar/bestand}}`

- Zoek naar nul of één keer een teken (optionele overeenkomst):

`egrep '{{a}}?' {{pad/naar/bestand}}`

- Zoek naar 10 herhalingen van een teken:

`egrep '{{a}}{10}' {{pad/naar/bestand}}`

- Zoek naar 3 tot 7 herhalingen van een karakter:

`egrep '{{a}}{3,7}' {{pad/naar/bestand}}`

- Zoek naar één van de vermelde opties:

`egrep '{{cat}}|{{dog}}|{{mouse}}' {{pad/naar/bestand}}`

- Zoek naar één van de vermelde opties binnen een groter patroon:

`egrep 'c({{a}}|{{o}}|{{u}})p' {{pad/naar/bestand}}`

- Zoek naar een groep tekens die één of meerdere keren herhaald worden:

`egrep '({{aeiou}})+' {{pad/naar/bestand}}`

- Zoek naar speciale tekenklassen (meer informatie: <https://www.regular-expressions.info/posixbrackets.html>):

`egrep [[{{:alnum:|:alpha:|:space:|...}}]] {{pad/naar/bestand}}`
