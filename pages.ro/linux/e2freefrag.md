# e2freefrag

> Imprimaţi informaţiile despre fragmentarea spaţiului liber pentru sistemele de fişiere ext2/ext3/ext4.
> Mai multe informaţii: <https://manned.org/e2freefrag>

- Verificați câte blocuri libere sunt prezente ca spațiu liber contiguu și aliniat:

`e2freefrag {{/dev/sdXN}}`

- Specificați dimensiunea bucăților în kiloocteți pentru a imprima câte bucăți gratuite sunt disponibile:

`e2freefrag -c {{chunk_size_in_kb}} {{/dev/sdXN}}`
