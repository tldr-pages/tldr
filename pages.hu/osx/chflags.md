# chflags

> Fájl- vagy könyvtárjelzők módosítása. További információ: <https://ss64.com/osx/chflags.html>.

- A `hidden` jelző beállítása egy fájlhoz:

`chflags {{hidden}} {{path/to/file}}`

- A `hidden` jelző visszavonása egy fájlhoz:

`chflags {{nohidden}} {{path/to/file}}`

- A `uchg` jelző rekurzív beállítása egy könyvtárhoz:

`chflags -R {{uchg}} {{path/to/directory}}`

- A `uchg` zászló rekurzív visszavonása egy könyvtár esetében:

`chflags -R {{nouchg}} {{path/to/directory}}`
