# lilypond

> Tastați muzică și/sau produceți MIDI din fișier.
> Mai multe informaţii: <https://lilypond.org>

- Compilați un fișier lilypond într-un PDF:

`lilypond {{path/to/file}}`

- Compilați în formatul specificat:

`lilypond --formats={{format_dump}} {{path/to/file}}`

- Compilați fișierul specificat, suprimarea actualizărilor de progres:

`lilypond -s {{path/to/file}}`

- Compilați fișierul specificat și specificați, de asemenea, numele fișierului de ieșire:

`lilypond --output={{path/to/output_file}} {{path/to/input_file}}`

- Afișați versiunea curentă a lilypond:

`lilypond --version`
