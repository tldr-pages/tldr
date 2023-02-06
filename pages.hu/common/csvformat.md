# csvformat

> CSV fájl átalakítása egyéni kimeneti formátumba. A csvkit része. További információ: <https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html>.

- Konvertálás tabulátorral elválasztott fájlba (TSV):

`csvformat -T {{data.csv}}`

- Az elhatárolójelek átalakítása egyéni karakterré:

`csvformat -D "{{custom_character}}" {{data.csv}}`

- A sorvégek átalakítása kocsivisszatérré (^M) + sortovábbítássá:

`csvformat -M "{{\r\n}}" {{data.csv}}`

- Idézőjelek használatának minimalizálása:

`csvformat -U 0 {{data.csv}}`

- Az idézőjelek használatának maximalizálása:

`csvformat -U 1 {{data.csv}}`
