# wasm-objdump

> WebAssembly binárisokból származó információk megjelenítése. További információ: <https://github.com/WebAssembly/wabt>.

- Egy adott bináris állomány szakaszfejlécének megjelenítése:

`wasm-objdump -h {{file.wasm}}`

- Egy adott bináris teljes szétszerelt kimeneteinek megjelenítése:

`wasm-objdump -d {{file.wasm}}`

- Az egyes szakaszok részleteinek megjelenítése:

`wasm-objdump --details {{file.wasm}}`

- Egy adott szakasz részleteinek megjelenítése:

`wasm-objdump --section '{{import}}' --details {{file.wasm}}`
