# mmls

> Afișează structura partiției unui sistem de volum.
> Mai multe informaţii: <https://wiki.sleuthkit.org/index.php?title=Mmls>

- Afișează tabela de partiții stocată într-un fișier imagine:

`mmls {{path/to/image_file}}`

- Afișați tabela de partiții cu o coloană suplimentară pentru dimensiunea partiției:

`mmls -B -i {{path/to/image_file}}`

- Afișați tabela de partiții într-o imagine EWF divizată:

`mmls -i ewf {{image.e01}} {{image.e02}}`

- Afișare tabele de partiții imbricate:

`mmls -t {{nested_table_type}} -o {{offset}} {{path/to/image_file}}`
