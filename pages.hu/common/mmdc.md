# mmdc

> CLI a sellőhöz, egy domain-specifikus nyelvvel rendelkező diagramgeneráló eszközhöz. A sellő definíciós fájlját veszi bemenetként, és SVG, PNG vagy PDF fájlt generál kimenetként. További információ: <https://mermaid-js.github.io/mermaid/>.

- Egy fájlt a megadott formátumba konvertál (a fájlkiterjesztésből automatikusan meghatározásra kerül):

`mmdc --input {{input.mmd}} --output {{output.svg}}`

- Adja meg a diagram témáját:

`mmdc --input {{input.mmd}} --output {{output.svg}} --theme {{forest|dark|neutral|default}}`

- A diagram háttérszínének megadása (pl. `lime`, `"#D8064F"` vagy `transparent`):

`mmdc --input {{input.mmd}} --output {{output.svg}} --backgroundColor {{color}}`
