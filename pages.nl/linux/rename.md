# rename

> Hernoem meerdere bestanden.
> Opmerking: deze pagina verwijst naar het commando uit het `util-linux` pakket.
> Voor de Perl-versie, zie `file-rename` of `perl-rename`.
> Waarschuwing: Dit commando heeft geen beveiligingen en zal bestanden zonder waarschuwing overschrijven.
> Meer informatie: <https://manned.org/rename>.

- Hernoem bestanden door eenvoudige vervangingen (vervang 'foo' door 'bar' waar dan ook gevonden):

`rename {{foo}} {{bar}} {{*}}`

- Test - toon welke hernoemingen zouden plaatsvinden zonder ze werkelijk uit te voeren:

`rename {{[-vn|--verbose --no-act]}} {{foo}} {{bar}} {{*}}`

- Overschrijf geen bestaande bestanden:

`rename {{[-o|--no-overwrite]}} {{foo}} {{bar}} {{*}}`

- Verander bestandsextensies:

`rename {{.ext}} {{.bak}} {{*.ext}}`

- Voeg "foo" toe aan alle bestandsnamen in de huidige directory:

`rename {{''}} {{'foo'}} {{*}}`

- Hernoem een groep opeenvolgend genummerde bestanden door de nummers tot 3 cijfers te vullen met nullen:

`rename {{foo}} {{foo00}} {{foo?}} && rename {{foo}} {{foo0}} {{foo??}}`
