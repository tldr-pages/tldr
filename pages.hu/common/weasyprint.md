# weasyprint

> A HTML PDF vagy PNG formátumba történő átalakítása. További információ: <https://weasyprint.org/>.

- HTML fájl átalakítása PDF-be:

`weasyprint {{path/to/input.html}} {{path/to/output}}.pdf`

- HTML-fájl PNG-be történő renderelése, egy további felhasználói stílustáblával együtt:

`weasyprint {{path/to/input.html}} {{path/to/output}}.png --stylesheet {{path/to/stylesheet.css}}`

- További hibakeresési információk kiadása a renderelés során:

`weasyprint {{path/to/input.html}} {{path/to/output}}.pdf --verbose`

- Egyéni felbontás megadása PNG-kijuttatáskor:

`weasyprint {{path/to/input.html}} {{path/to/output}}.png --resolution {{300}}`

- Alap-URL megadása a bemeneti HTML-fájlban található relatív URL-címekhez:

`weasyprint {{path/to/input.html}} {{path/to/output}}.png --base-url {{url_or_filename}}`
