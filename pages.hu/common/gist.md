# gist

> Kód feltöltése a https://gist.github.com. További információ: <https://github.com/defunkt/gist>.

- Jelentkezzen be a gistbe ezen a számítógépen:

`gist --login`

- Gist létrehozása tetszőleges számú szöveges fájlból:

`gist {{file.txt}} {{file2.txt}}`

- Hozzon létre egy privát gistet egy leírással:

`gist --private --description "{{A meaningful description}}" {{file.txt}}`

- Olvassa be a `stdin` tartalmát, és hozzon létre belőle gistet:

`{{echo "hello world"}} | gist`

- A nyilvános és a privát gistek listázása:

`gist --list`

- Bármely felhasználó összes nyilvános gistjének listázása:

`gist --list {{username}}`

- Egy gist frissítése az URL-ből származó azonosítóval:

`gist --update {{GIST_ID}} {{file.txt}}`
