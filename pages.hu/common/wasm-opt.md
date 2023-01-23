# wasm-opt

> WebAssembly bináris fájlok optimalizálása. További információ: <https://github.com/webassembly/binaryen>.

- Alapértelmezett optimalizációk alkalmazása és írás egy adott fájlba:

`wasm-opt -O {{input.wasm}} -o {{output.wasm}}`

- Alkalmazza az összes optimalizálást és írjon egy adott fájlba (több időt vesz igénybe, de optimális kódot generál):

`wasm-opt -O4 {{input.wasm}} -o {{output.wasm}}`

- Optimalizálja a fájlt a méretre:

`wasm-opt -Oz {{input.wasm}} -o {{output.wasm}}`

- A bináris fájl szöveges ábrázolását kiírja a konzolra:

`wasm-opt {{input.wasm}} --print`
