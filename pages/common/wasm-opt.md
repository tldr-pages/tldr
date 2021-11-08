# wasm-opt

> Optimize WebAssembly binary files.
> More information: <https://github.com/webassembly/binaryen>.

- Apply default optimizations and write to a given file:

`wasm-opt -O {{input.wasm}} -o {{output.wasm}}`

- Apply all optimizations and write to a given file (takes more time, but generates optimal code):

`wasm-opt -O4 {{input.wasm}} -o {{output.wasm}}`

- Optimize a file for size:

`wasm-opt -Oz {{input.wasm}} -o {{output.wasm}}`

- Print the textual representation of the binary to console:

`wasm-opt {{input.wasm}} --print`
