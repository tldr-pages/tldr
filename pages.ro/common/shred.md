# shred

> Suprascrieți fișierele pentru a șterge în siguranță datele.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/shred>

- Suprascrie un fișier:

`shred {{file}}`

- Suprascrie un fișier, lăsând zerouri în loc de date aleatorii:

`shred --zero {{file}}`

- Suprascrie un fișier de 25 de ori:

`shred -n25 {{file}}`

- Suprascrie un fișier și eliminați-l:

`shred --remove {{file}}`
