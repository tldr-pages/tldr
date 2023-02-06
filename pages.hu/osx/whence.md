# whence

> A zsh beépített parancssor, amely jelzi, hogy egy adott parancsot hogyan értelmezzen. További információ: <https://www.unix.com/man-page/OpenSolaris/1/whence/>.

- Interpret {{command}}, bővítéssel, ha a `alias` (hasonlóan a `command -v` builtinhez):

`whence "{{command}}"`

- A {{parancs}} típusának megjelenítése, helymeghatározással, ha függvényként vagy binárisan definiált (a `type` és a `command -V` builtinekkel egyenértékű):

`whence -v "{{command}}"`

- Ugyanaz, mint fent, kivéve a shell függvények tartalmának megjelenítése a hely helyett (a `which` builtinnel egyenértékű):

`whence -c "{{command}}"`

- Ugyanaz, mint a fentiekben, de a parancs összes előfordulását megjeleníti a parancs útvonalán (a `where` beépített programmal egyenértékű):

`whence -ca "{{command}}"`

- Csak a `PATH` címen keres a {{command}}-ra, figyelmen kívül hagyva a builtineket, aliasokat vagy shellfüggvényeket (megegyezik a `where` paranccsal):

`whence -p "{{command}}"`
