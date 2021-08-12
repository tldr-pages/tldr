# touch

> Modificați timpii de acces și modificare a unui fișier (atime, mtime).
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/touch>

- Creați un fișier (e) nou (e) gol (e) sau modificați orele pentru fișierele existente la ora curentă:

`touch {{filename}}`

- Setați orele pe un fișier la o anumită dată și oră:

`touch -t {{YYYYMMDDHHMM.SS}} {{filename}}`

- Utilizați orele dintr-un fișier pentru a seta orele pe un al doilea fișier:

`touch -r {{filename}} {{filename2}}`

- Creați mai multe fișiere:

`touch {{file{1,2,3}.txt}}`
