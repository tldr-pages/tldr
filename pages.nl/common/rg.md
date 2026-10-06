# rg

> Ripgrep, een recursieve regel-georiënteerde zoektool.
> Wil een sneller alternatief zijn dan `grep`.
> Meer informatie: <https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md>.

- Zoek recursief in de huidige map naar een patroon (`regex`):

`rg {{patroon}}`

- Zoek recursief naar een patroon in een bestand of map:

`rg {{patroon}} {{pad/naar/bestand_of_map}}`

- Zoek naar een letterlijk string patroon:

`rg {{[-F|--fixed-strings]}} -- {{string}}`

- Voeg verborgen bestanden en onderdelen van de `.gitignore` toe:

`rg {{[-.|--hidden]}} --no-ignore {{patroon}}`

- Zoek in bestanden die overeenkomen met een `glob` (bijv. `README.*`, gebruik `!bestandsnaam_patroon` om in plaats daarvan uit te sluiten) naar een patroon:

`rg {{patroon}} {{[-g|--glob]}} '{{bestandsnaam_glob_patroon}}'`

- Toon recursief de bestandsnamen in de huidige map en markeer degene die overeenkomen met een patroon:

`rg --files | rg {{[--passthru|--passthrough]}} {{patroon}}`

- Toon alleen overeenkomende bestanden (handig bij het doorsturen naar andere commando's):

`rg {{[-l|--files-with-matches]}} {{patroon}}`

- Toon regels die niet overeenkomen met het patroon:

`rg {{[-v|--invert-match]}} {{patroon}}`
