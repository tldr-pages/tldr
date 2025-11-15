# ack

> Een zoektool zoals grep, geoptimaliseerd voor ontwikkelaars.
> Zie ook: `rg`, dat is veel sneller.
> Meer informatie: <https://beyondgrep.com/documentation>.

- Zoek recursief naar bestanden met een tekenreeks of reguliere expressie in de huidige map:

`ack "{{zoekpatroon}}"`

- Zoek naar een niet-hoofdlettergevoelig patroon:

`ack {{[-i|--ignore-case]}} "{{zoekpatroon}}"`

- Zoek naar lijnen die overeenkomen met een patroon en druk alleen de overeenkomende tekst af en niet de rest van de lijn:

`ack {{[-o|--output='$&']}} "{{zoekpatroon}}"`

- Beperk het zoeken tot bestanden van een specifiek type:

`ack {{[-t|--type]}} {{ruby}} "{{zoekpatroon}}"`

- Zoek niet in bestanden van een specifiek type:

`ack {{[-t|--type]}} no{{ruby}} "{{zoekpatroon}}"`

- Tel het totaal aantal gevonden matches:

`ack {{[-c|--count]}} {{[-h|--no-filename]}} "{{zoekpatroon}}"`

- Toon alleen voor elk bestand de bestandsnamen en het aantal overeenkomsten:

`ack {{[-c|--count]}} {{[-l|--files-with-matches]}} "{{zoekpatroon}}"`

- Maak een lijst van alle waarden die kunnen worden gebruikt met `--type`:

`ack --help-types`
