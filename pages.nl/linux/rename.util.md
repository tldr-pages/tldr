# rename

> Hernoem meerdere bestanden.
> WAARSCHUWING: dit commando overschrijft bestanden zonder te vragen, tenzij de `--no-act` optie wordt gebruikt.
> Opmerking: deze pagina verwijst naar het commando uit het `util-linux` pakket.
> Meer informatie: <https://manned.org/rename>.

- Hernoem bestanden met eenvoudige vervangingen (vervang een string door een vervanging waar het ook gevonden wordt):

`rename {{string}} {{vervanging}} {{*}}`

- Simuleer het uitvoeren van het programma zonder iets te doen:

`rename {{[-vn|--verbose --no-act]}} {{string}} {{vervanging}} {{*}}`

- Overschrijf geen bestaande bestanden:

`rename {{[-o|--no-overwrite]}} {{string}} {{vervanging}} {{*}}`

- Wijzig bestandsextensies:

`rename {{.ext}} {{.bak}} {{*.ext}}`

- Voeg een voorvoegsel toe aan het begin van alle bestandsnamen in de huidige map:

`rename '' '{{voorvoegsel}}' {{*}}`

- Hernoem een groep opeenvolgend genummerde bestanden met nul-opvulling van de nummers tot 3 cijfers:

`rename {{voorvoegsel}} {{voorvoegsel00}} {{voorvoegsel?}} && rename {{voorvoegsel}} {{voorvoegsel0}} {{voorvoegsel??}}`
