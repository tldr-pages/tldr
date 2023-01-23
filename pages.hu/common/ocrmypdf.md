# ocrmypdf

> Keresésre alkalmas PDF vagy PDF/A generálása szkennelt PDF-ből vagy szöveges képből. További információ: <https://ocrmypdf.readthedocs.io/en/latest/cookbook.html>.

- Új kereshető PDF/A fájl létrehozása beolvasott PDF- vagy képfájlból:

`ocrmypdf {{path/to/input_file}} {{path/to/output.pdf}}`

- Egy beolvasott PDF-fájl helyettesítése kereshető PDF-fájllal:

`ocrmypdf {{path/to/file.pdf}} {{path/to/file.pdf}}`

- Vegyes formátumú bemeneti PDF-fájl olyan oldalainak kihagyása, amelyek már szöveget tartalmaznak:

`ocrmypdf --skip-text {{path/to/input.pdf}} {{path/to/output.pdf}}`

- Egy rosszul beolvasott fájl oldalainak tisztítása, ferdítésmentesítése és elforgatása:

`ocrmypdf --clean --deskew --rotate-pages {{path/to/input_file}} {{path/to/output.pdf}}`

- A kereshető PDF-fájl metaadatainak beállítása:

`ocrmypdf --title "{{title}}" --author "{{author}}" --subject "{{subject}}" --keywords "{{keyword; key phrase; ...}}" {{path/to/input_file}} {{path/to/output.pdf}}`

- Súgó megjelenítése:

`ocrmypdf --help`
