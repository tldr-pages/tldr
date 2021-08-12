# resize2fs

> Redimensionați un sistem de fișiere ext2, ext3 sau ext4.
> Nu redimensionează partiția de bază, iar sistemul de fișiere trebuie demontat.

- Redimensionarea automată a unui sistem de fișiere:

`resize2fs {{/dev/sdXN}}`

- Redimensionați sistemul de fișiere la o dimensiune de 40G, afișând o bară de progres:

`resize2fs -p {{/dev/sdXN}} {{40G}}`

- Micșorați sistemul de fișiere la dimensiunea minimă posibilă:

`resize2fs -M {{/dev/sdXN}}`
