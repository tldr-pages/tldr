# truncate

> Micșorați sau extindeți dimensiunea unui fișier la dimensiunea specificată.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/truncate>

- Setați o dimensiune de 10 GB într-un fișier existent sau creați un fișier nou cu dimensiunea specificată:

`truncate --size {{10G}} {{filename}}`

- Extindeți dimensiunea fișierului cu 50M, umpleți cu găuri (care citește ca zero octeți):

`truncate --size +{{50M}} {{filename}}`

- Micșorați fișierul cu 2GiB, eliminând datele de la sfârșitul fișierului:

`truncate --size -{{2G}} {{filename}}`

- Goliți conținutul fișierului:

`truncate --size 0 {{filename}}`

- Goliți conținutul fișierului, dar nu creați fișierul dacă acesta nu există:

`truncate --no-create --size 0 {{filename}}`
