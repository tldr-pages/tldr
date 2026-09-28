# rename

> Hernoem meerdere bestanden.
> WAARSCHUWING: dit commando overschrijft bestanden zonder te vragen, tenzij de dry-run optie wordt gebruikt.
> Opmerking: deze pagina verwijst naar het commando uit het `util-linux` pakket.
> Meer informatie: <https://manned.org/rename>.

- Hernoem bestanden met eenvoudige vervangingen (vervang `foo` door `bar` waar het ook gevonden wordt):

`rename {{foo}} {{bar}} {{*}}`

- Simuleer het uitvoeren van het programma zonder iets te doen:

`rename {{[-vn|--verbose --no-act]}} {{foo}} {{bar}} {{*}}`

- Overschrijf geen bestaande bestanden:

`rename {{[-o|--no-overwrite]}} {{foo}} {{bar}} {{*}}`

- Wijzig bestandsextensies:

`rename {{.ext}} {{.bak}} {{*.ext}}`

- Voeg "foo" toe aan het begin van alle bestandsnamen in de huidige map:

`rename '' '{{foo}}' {{*}}`

- Hernoem een groep opeenvolgend genummerde bestanden met nul-opvulling van de nummers tot 3 cijfers:

`rename {{foo}} {{foo00}} {{foo?}} && rename {{foo}} {{foo0}} {{foo??}}`
