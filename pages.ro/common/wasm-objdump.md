# wasm-objdump

> Afișează informații din binarele WebaseMbly.

- Afișează anteturile secțiunii unui binar dat:

`wasm-objdump -h {{file.wasm}}`

- Afișează întreaga ieșire dezasamblată a unui binar dat:

`wasm-objdump -d {{file.wasm}}`

- Afișează detaliile fiecărei secțiuni:

`wasm-objdump --details {{file.wasm}}`

- Afișați detaliile unei secțiuni date:

`wasm-objdump --section '{{import}}' --details {{file.wasm}}`
