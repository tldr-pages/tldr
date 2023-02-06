# lshw

> Részletes információk listázása a hardverkonfigurációkról root felhasználóként. További információk: <https://manned.org/lshw>.

- Indítsa el a GUI-t:

`sudo lshw -X`

- Az összes hardver felsorolása táblázatos formában:

`sudo lshw -short`

- Az összes lemez és tárolóvezérlő listázása táblázatos formában:

`sudo lshw -class disk -class storage -short`

- Az összes hálózati interfész mentése HTML-fájlba:

`sudo lshw -class network -html > {{interfaces.html}}`
