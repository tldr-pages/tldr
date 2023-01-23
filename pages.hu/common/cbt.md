# cbt

> Segédprogram a Google Cloud's Bigtable adatainak kiolvasásához. További információ: <https://cloud.google.com/bigtable/docs/cbt-reference>.

- Az aktuális projektben lévő táblázatok listázása:

`cbt ls`

- Az aktuális projekt egy adott táblájában lévő sorok számának kiírása:

`cbt count "{{table_name}}"`

- Egy adott táblázat egyetlen sorának megjelenítése az aktuális projektben, oszloponként csak 1 (legfrissebb) cellaváltozással:

`cbt lookup "{{table_name}}" "{{row_key}}" cells-per-column={{1}}`

- Egyetlen sor megjelenítése csak egy adott oszlop(ok)kal (a teljes család visszaadásához hagyja ki a minősítőt) az aktuális projektben:

`cbt lookup "{{table_name}}" "{{row_key}}" columns="{{family1:qualifier1,family2:qualifier2,...}}"`

- Legfeljebb 5 sor keresése az aktuális projektben egy adott regex minta alapján, és ezek kinyomtatása:

`cbt read "{{table_name}}" regex="{{row_key_pattern}}" count={{5}}`

- A sorok egy adott tartományának beolvasása és csak a visszaadott sorkulcsok nyomtatása az aktuális projektben:

`cbt read {{table_name}} start={{start_row_key}} end={{end_row_key}} keys-only=true`
