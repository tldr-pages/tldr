# wasm-opt

> Optimizați fișierele binare WebaseMbly.

- Aplicați optimizări implicite și scrieți într-un fișier dat:

`wasm-opt -O {{input.wasm}} -o {{output.wasm}}`

- Aplicați toate optimizările și scrieți într-un anumit fișier (durează mai mult timp, dar generează cod optim):

`wasm-opt -O4 {{input.wasm}} -o {{output.wasm}}`

- Optimizarea unui fișier pentru dimensiune:

`wasm-opt -Oz {{input.wasm}} -o {{output.wasm}}`

- Imprimați reprezentarea textuală a binarului la consola:

`wasm-opt {{input.wasm}} --print`
