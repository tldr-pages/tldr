# rg

> Ripgrep, een recursieve regel-georiënteerde zoek tool.
> Wil een sneller alternatief zijn dan `grep`.
> Meer informatie: <https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md>.

- Zoek recursief in de huidige map naar een patroon (reguliere expressie):

`rg {{patroon}}`

- Zoek recursief naar een patroon in een bestand of map:

`rg {{patroon}} {{pad/naar/bestand_of_map}}`

- Voeg verborgen bestanden en onderdelen van de `.gitignore` toe:

`rg {{[-.|--hidden]}} --no-ignore {{patroon}}`

- Zoek in bestanden die overeenkomen met een glob (bijv. `README.*`) naar een patroon:

`rg {{patroon}} {{[-g|--glob]}} {{bestandsnaam_glob_patroon}}`

- Toon recursief de bestandsnamen welke overeenkomen met een pattern:

`rg --files | rg {{patroon}}`

- Toon alleen overeenkomende bestanden (handig bij het doorsturen naar andere commando's):

`rg {{[-l|--files-with-matches]}} {{patroon}}`

- Toon regels die niet overeenkomen met de gegeven reguliere expressie:

`rg {{[-v|--invert-match]}} {{patroon}}`

- Zoek naar een letterlijk string pattroon:

`rg {{[-D|--fixed-strings]}} -- {{string}}`
