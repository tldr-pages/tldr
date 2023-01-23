# just

> V8 JavaScript futtató Linuxra. További információ: <https://github.com/just-js/just>.

- Indítson el egy REPL-t (interaktív shell):

`just`

- Egy JavaScript fájl futtatása:

`just {{path/to/file.js}}`

- JavaScript kód kiértékelése a kód argumentumként való átadásával:

`just eval "{{code}}"`

- Új projekt inicializálása egy azonos nevű könyvtárban:

`just init {{project_name}}`

- Egy JavaScript-alkalmazás futtatható állományba építése:

`just build {{path/to/file.js}} --static`
