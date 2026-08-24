# colorpicker

> Colorpicker minimalista per X11.
> Qualsiasi gesto del mouse eccetto `<LeftClick>` terminerà il programma.
> Maggiori informazioni: <https://github.com/ym1234/colorpicker>.

- Avvia colorpicker e stampa il valore esadecimale e RGB di ogni pixel cliccato su `stdout`:

`colorpicker`

- Stampa il colore di un solo pixel cliccato e poi termina:

`colorpicker --one-shot`

- Stampa il colore di ogni pixel cliccato e termina quando viene premuto un tasto:

`colorpicker --quit-on-keypress`

- Stampa solo il valore RGB:

`colorpicker --rgb`

- Stampa solo il valore esadecimale:

`colorpicker --hex`
