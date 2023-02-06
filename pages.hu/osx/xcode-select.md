# xcode-select

> Váltás az Xcode és a mellékelt fejlesztői eszközök különböző verziói között. Az Xcode elérési útvonalának frissítésére is használható, ha a telepítés után áthelyezik. További információ: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Az Xcode parancssori eszközeinek telepítése:

`xcode-select --install`

- Adott elérési útvonal kiválasztása aktív fejlesztői könyvtárként:

`xcode-select --switch {{path/to/Xcode.app/Contents/Developer}}`

- Kiválaszt egy adott Xcode-példányt, és annak fejlesztői könyvtárát használja aktív könyvtárként:

`xcode-select --switch {{path/to/Xcode.app}}`

- Az aktuálisan kiválasztott fejlesztői könyvtár kinyomtatása:

`xcode-select --print-path`

- A felhasználó által megadott fejlesztői könyvtár elvetése, hogy az alapértelmezett keresési mechanizmuson keresztül találja meg:

`sudo xcode-select --reset`
