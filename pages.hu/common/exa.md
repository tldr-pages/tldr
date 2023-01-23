# exa

> A `ls` (List directory contents) modern helyettesítője. További információ: <https://the.exa.website>.

- Fájlok soronkénti felsorolása:

`exa --oneline`

- Az összes fájl listázása, beleértve a rejtett fájlokat is:

`exa --all`

- Az összes fájl hosszú formátumú listája (jogosultságok, tulajdonjog, méret és módosítási dátum):

`exa --long --all`

- Fájlok listázása a legnagyobbal a tetején:

`exa --reverse --sort={{size}}`

- A fájlok fájának megjelenítése, három szint mélységben:

`exa --long --tree --level={{3}}`

- A fájlok listája módosítási dátum szerint rendezve (a legrégebbi előbbre):

`exa --long --sort={{modified}}`

- Fájlok listázása fejléccel, ikonokkal és Git-státusszal:

`exa --long --header --icons --git`

- Nem listázza a `.gitignore` oldalon említett fájlokat:

`exa --git-ignore`
