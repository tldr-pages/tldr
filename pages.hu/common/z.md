# z

> Nyomon követi a leggyakrabban használt (frekventált) könyvtárakat, és lehetővé teszi a gyors navigációt hozzájuk karakterlánc-minták vagy reguláris kifejezések segítségével. További információ: <https://github.com/rupa/z>.

- Olyan könyvtárba megyünk, amelynek nevében szerepel a "foo":

`z {{foo}}`

- Olyan könyvtárba lépni, amelynek a nevében szerepel a "foo", majd a "bar":

`z {{foo}} {{bar}}`

- A "foo"-nak megfelelő legmagasabb rangú könyvtárba megy:

`z -r {{foo}}`

- A "foo"-nak megfelelő, legutóbb megnyitott könyvtárba lép:

`z -t {{foo}}`

- A `z` adatbázisában található összes olyan könyvtár listázása, amely megfelel a "foo"-nak:

`z -l {{foo}}`

- Az aktuális könyvtár eltávolítása a `z` adatbázisából:

`z -x .`

- A találatok korlátozása az aktuális könyvtár alkönyvtáraira:

`z -c {{foo}}`
