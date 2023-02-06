# rename

> Több fájl átnevezése.
> MEGJEGYZÉS: ez az oldal a `util-linux` csomagban található parancsra vonatkozik.
> A Perl verzióért lásd a `file-rename` vagy a `perl-rename`.
> Figyelmeztetés: Ez a parancs nem rendelkezik biztosítékokkal, és kérdezés nélkül felülírja a fájlokat.
> További információ: <https://manned.org/rename>.

- Fájlok átnevezése egyszerű helyettesítésekkel (a 'foo' helyett 'bar', ahol csak található):

`rename {{foo}} {{bar}} {{*}}`

- Szárazfutás - megjeleníti, hogy mely átnevezések történnének anélkül, hogy végrehajtaná azokat:

`rename -vn {{foo}} {{bar}} {{*}}`

- Ne írja felül a meglévő fájlokat:

`rename -o {{foo}} {{bar}} {{*}}`

- Fájlkiterjesztések módosítása:

`rename {{.ext}} {{.bak}} {{*.ext}}`

- Az aktuális könyvtárban lévő összes fájlnévhez "foo" előtagot ad:

`rename {{''}} {{'foo'}} {{*}}`

- Egyre több számozott fájlok csoportjának átnevezése, a számokat 3 számjegyig nullázva:

`rename {{foo}} {{foo00}} {{foo?}} && rename {{foo}} {{foo0}} {{foo??}}`
