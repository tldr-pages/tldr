# kak

> Kakoune este un editor de cod bazat pe moduri care implementează paradigma „selecții multiple”.
> Datele pot fi selectate și editate simultan în locații diferite, utilizând mai multe selecții; utilizatorii se pot conecta, de asemenea, la aceeași sesiune pentru editare în colaborare.
> Mai multe informaţii: <https://kakoune.org>

- Deschideți un fișier și introduceți modul normal, pentru a executa comenzi:

`kak {{path/to/file}}`

- Introduceți modul de inserare din modul normal, pentru a scrie text în fișier:

`i`

- Modul de inserare de evacuare, pentru a reveni la modul normal:

`<Escape>`

- Înlocuiți toate instanțele de „foo” în fișierul curent cu „bar”:

`%s{{foo}}<Enter>c{{bar}}<Escape>`

- Un-selectați toate selecțiile secundare și păstrați numai cea principală:

`<Space>`

- Căutați numere și selectați primele două:

`/\d+<Enter>N`

- Introduceți conținutul unui fișier:

`!cat {{path/to/file}}<Enter>`

- Salvați fișierul curent:

`:w<Enter>`
