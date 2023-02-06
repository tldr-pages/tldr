# textutil

> Különböző formátumú szövegfájlok kezelésére szolgál. További információ: <https://ss64.com/osx/textutil.html>.

- Információk megjelenítése a `foo.rtf` címen:

`textutil -info {{foo.rtf}}`

- A `foo.rtf` átalakítása a `foo.html` címre:

`textutil -convert {{html}} {{foo.rtf}}`

- Rich text átalakítása normál szöveggé:

`textutil {{foo.rtf}} -convert {{txt}}`

- A `foo.txt` átalakítása `foo.rtf`-re, Times 10 betűtípussal:

`textutil -convert {{rtf}} -font {{Times}} -fontsize {{10}} {{foo.txt}}`

- Az aktuális könyvtárban lévő összes RTF fájl betöltése, tartalmuk összekapcsolása, és az eredmény kiírása `index.html` formában, a HTML cím "Több fájl" beállításával:

`textutil -cat {{html}} -title "Several Files" -output {{index.html}} *.rtf`
