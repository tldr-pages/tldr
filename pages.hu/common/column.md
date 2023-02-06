# column

> A szabványos bemenet vagy egy fájl több oszlopra történő formázása. Az oszlopok a sorok előtt töltődnek ki; az alapértelmezett elválasztó egy szóköz. További információ: <https://manned.org/column>.

- Egy parancs kimenetének formázása 30 karakter széles kijelzőre:

`printf "header1 header2\nbar foo\n" | column --output-width {{30}}`

- Az oszlopok automatikus felosztása és automatikus igazítása táblázatos formátumban:

`printf "header1 header2\nbar foo\n" | column --table`

- Adja meg az oszlopelválasztó karaktert a `--table` opcióhoz (pl. "," CSV esetén) (alapértelmezés szerint szóköz):

`printf "header1,header2\nbar,foo\n" | column --table --separator {{,}}`

- Sorok kitöltése az oszlopok kitöltése előtt:

`printf "header1\nbar\nfoobar\n" | column --output-width {{30}} --fillrows`
