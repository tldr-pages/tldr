# findstr

> Megadott szöveg keresése egy vagy több fájlban. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/findstr>.

- Szóközzel elválasztott karakterlánc(ok) keresése az összes fájlban:

`findstr "{{query}}" *`

- Szóközzel elválasztott karakterlánc(ok) keresése egy piped parancs kimenetén:

`{{dir}} | findstr "{{query}}"`

- Szóközzel elválasztott karakterlánc(ok) keresése minden fájlban ismétlődően:

`findstr /s "{{query}}" *`

- A karakterláncok keresése nagy- és kisbetűket nem érzékelő kereséssel:

`findstr /i "{{query}}" *"`

- Szövegek keresése az összes fájlban reguláris kifejezések használatával:

`findstr /r "{{expression}}" *`

- Szó szerinti (szóközöket tartalmazó) karakterlánc keresése az összes szöveges fájlban:

`findstr /c:"{{query}}" *.txt`

- A sorszám megjelenítése minden egyes megfelelő sor előtt:

`findstr /n "{{query}}" *`

- Csak az egyezést tartalmazó fájlnevek megjelenítése:

`findstr /m "{{query}}" *`
