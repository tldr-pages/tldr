# dot

> Strumento da linea di comando per produrre disegni a livelli di grafi orientati.
> Maggiori informazioni: <https://graphviz.org/doc/info/command.html>.

- Renderizza un'immagine determinando il nome del file di output dal nome del file di input ed il formato:

`dot -Tpng -O {{percorso/al/file.dot}}`

- Crea una SVG da un file DOT:

`dot -Tsvg -o {{percorso/al/file_output.svg}} {{percorso/al/file.dot}}`
