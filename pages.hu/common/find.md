# find

> Fájlok vagy könyvtárak keresése a megadott könyvtárfa alatt, rekurzív módon. További információ: <https://manned.org/find>.

- Fájlok keresése kiterjesztés alapján:

`find {{root_path}} -name '{{*.ext}}'`

- Több útvonal/nevet tartalmazó mintának megfelelő fájlok keresése:

`find {{root_path}} -path '{{**/path/**/*.ext}}' -or -name '{{*pattern*}}'`

- Adott névnek megfelelő könyvtárak keresése, a nagy- és kisbetűket nem érzékelő módban:

`find {{root_path}} -type d -iname '{{*lib*}}'`

- Adott mintának megfelelő fájlok keresése, bizonyos elérési utak kizárásával:

`find {{root_path}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Megadott mérettartománynak megfelelő fájlok keresése, a rekurzív mélység "1"-re történő korlátozásával::

`find {{root_path}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Futtasson egy parancsot minden egyes fájlhoz (a fájlnév eléréséhez használja a `{}` címet a parancson belül):

`find {{root_path}} -name '{{*.ext}}' -exec {{wc -l {} }}\;`

- Az elmúlt 7 napban módosított fájlok keresése:

`find {{root_path}} -daystart -mtime -{{7}}`

- Üres (0 bájtos) fájlok keresése és törlése:

`find {{root_path}} -type {{f}} -empty -delete`
