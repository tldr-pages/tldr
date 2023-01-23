# mktemp

> Ideiglenes fájl vagy könyvtár létrehozása. További információ: <https://www.gnu.org/software/autogen/mktemp.html>.

- Hozzon létre egy üres ideiglenes fájlt, és írja ki az abszolút elérési útvonalat:

`mktemp`

- Üres ideiglenes fájl létrehozása adott utótaggal, és a fájl abszolút elérési útjának kiírása:

`mktemp --suffix "{{.ext}}"`

- Ideiglenes könyvtár létrehozása és a könyvtár abszolút elérési útjának kiírása:

`mktemp --directory`
