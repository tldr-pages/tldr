# ncc

> Egy Node.js alkalmazás egyetlen fájlba fordítása. Támogatja a TypeScriptet, a bináris kiegészítőket és a dinamikus követelményeket. További információ: <https://github.com/vercel/ncc>.

- Node.js alkalmazás csomagolása:

`ncc build {{path/to/file.js}}`

- Egy Node.js alkalmazás csomagolása és kicsinyítése:

`ncc build --minify {{path/to/file.js}}`

- Egy Node.js alkalmazás csomagolása és kicsinyítése, valamint forrástérképek generálása:

`ncc build --source-map {{path/to/file.js}}`

- Automatikus újrakompilálás a forrásfájlok módosításakor:

`ncc build --watch {{path/to/file.js}}`

- Node.js alkalmazás csomagolása egy ideiglenes könyvtárba és futtatása tesztelés céljából:

`ncc run {{path/to/file.js}}`

- A `ncc` gyorsítótár megtisztítása:

`ncc clean cache`
