# wasm2c

> Egy fájl átalakítása a WebAssembly bináris formátumból C forrásfájlba és fejlécbe. További információ: <https://github.com/WebAssembly/wabt>.

- Egy fájl átalakítása C forrásfájllá és fejléccé, majd megjelenítése a konzolon:

`wasm2c {{file.wasm}}`

- A kimenet kiírása egy adott fájlba (`file.h` kap plusz generálást):

`wasm2c {{file.wasm}} -o {{file.c}}`
