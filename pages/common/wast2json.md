# wast2json

> Convert a file in the WebAssembly spec test format to JSON and associated WebAssembly binary files.
> More information: <https://webassembly.github.io/wabt/doc/wast2json.1.html>.

- Convert a `.wast` file to a JSON file and associated `.wasm` binary files:

`wast2json {{path/to/file.wast}}`

- Convert a file and write the JSON output to a specific file:

`wast2json {{path/to/file.wast}} {{[-o|--output]}} {{path/to/file.json}}`

- Create relocatable WebAssembly binaries (suitable for linking):

`wast2json {{path/to/file.wast}} {{[-r|--relocatable]}}`

- Include debug names in the generated binary files:

`wast2json {{path/to/file.wast}} --debug-names`

- Convert a file, enabling all WebAssembly features:

`wast2json {{path/to/file.wast}} --enable-all`
