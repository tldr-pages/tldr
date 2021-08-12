# weasyprint

> Randare HTML în PDF sau PNG.
> Mai multe informaţii: <https://weasyprint.org/>

- Randarea unui fișier HTML în PDF:

`weasyprint {{path/to/input.html}} {{path/to/output}}.pdf`

- Randați un fișier HTML la PNG, inclusiv o foaie de stil de utilizator suplimentar:

`weasyprint {{path/to/input.html}} {{path/to/output}}.png --stylesheet {{path/to/stylesheet.css}}`

- Ieșiți informații suplimentare de depanare la randare:

`weasyprint {{path/to/input.html}} {{path/to/output}}.pdf --verbose`

- Specificați o rezoluție personalizată atunci când se trimite la PNG:

`weasyprint {{path/to/input.html}} {{path/to/output}}.png --resolution {{300}}`

- Specificați un URL de bază pentru adresele URL relative în fișierul HTML de intrare:

`weasyprint {{path/to/input.html}} {{path/to/output}}.png --base-url {{url_or_filename}}`
