# rg

> Ripgrep is een recursieve regel-georiënteerde zoek tool.
> Wil een sneller alternatief zijn dan `grep`.
> Meer informatie: <https://github.com/BurntSushi/ripgrep>.

- Zoek recursief in de huidige map naar een reguliere expressie:

`rg {{reguliere_expressie}}`

- Zoek recursief in de huidige map naar een reguliere expressie, inclusief verborgen bestanden en bestanden opgenomen in `.gitignore`:

`rg --no-ignore --hidden {{reguliere_expressie}}`

- Zoek alleen in een subset van mappen naar een reguliere expressie:

`rg {{reguliere_expressie}} {{set_van_submappen}}`

- Zoek in bestanden die overeenkomen met een glob (bijv. `README.*`) naar een reguliere expressie:

`rg {{reguliere_expressie}} --glob {{glob}}`

- Zoek naar bestandsnamen die overeenkomen met een reguliere expressie:

`rg --files | rg {{reguliere_expressie}}`

- Toon alleen overeenkomende bestanden (handig bij het doorsturen naar andere commando's):

`rg --files-with-matches {{reguliere_expressie}}`

- Toon regels die niet overeenkomen met de gegeven reguliere expressie:

`rg --invert-match {{reguliere_expressie}}`

- Zoek naar een letterlijk string pattroon:

`rg --fixed-strings -- {{string}}`
