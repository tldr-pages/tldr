# gcalcli

> Parancssori eszköz a Google Naptárral való interakcióhoz. Első indításkor Google API engedélyt kér. További információ: <https://github.com/insanum/gcalcli>.

- Az összes naptár eseményeinek listázása a következő 7 napban:

`gcalcli agenda`

- Megjeleníti a meghatározott dátumokkal kezdődő vagy azok közötti eseményeket (relatív dátumokat is elfogad, pl. "holnap"):

`gcalcli agenda {{mm/dd}} [{{mm/dd}}]`

- Egy adott naptár eseményeinek listázása:

`gcalcli --calendar {{calendar_name}} agenda`

- Az események ASCII-naptárának megjelenítése hetente:

`gcalcli calw`

- Havi események ASCII-naptárának megjelenítése:

`gcalcli calm`

- Esemény gyors hozzáadása a naptárhoz:

`gcalcli --calendar {{calendar_name}} quick "{{mm/dd}} {{HH:MM}} {{event_name}}"`

- Esemény hozzáadása a naptárhoz. Interaktív felszólítás kiváltása:

`gcalcli --calendar "{{calendar_name}}" add`
