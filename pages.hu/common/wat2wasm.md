# wat2wasm

> Egy fájl konvertálása a WebAssembly szöveges formátumból bináris formátumba. További információ: <https://github.com/WebAssembly/wabt>.

- Egy fájl elemzése és hibaellenőrzése:

`wat2wasm {{file.wat}}`

- A kimeneti bináris állomány kiírása egy adott fájlba:

`wat2wasm {{file.wat}} -o {{file.wasm}}`

- Minden egyes bájt egyszerűsített ábrázolása:

`wat2wasm -v {{file.wat}}`
