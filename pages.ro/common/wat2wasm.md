# wat2wasm

> Conversia unui fișier din formatul text WebaseMbly în formatul binar.
> Mai multe informaţii: <https://github.com/WebAssembly/wabt>

- Parsează și verifică un fișier pentru erori:

`wat2wasm {{file.wat}}`

- Scrieți binarul de ieșire într-un fișier dat:

`wat2wasm {{file.wat}} -o {{file.wasm}}`

- Afișează reprezentarea simplificată a fiecărui octet:

`wat2wasm -v {{file.wat}}`
