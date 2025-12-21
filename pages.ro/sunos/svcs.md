# svcs

> Listează informații despre serviciile care rulează.
> Mai multe informații: <https://www.unix.com/man-page/linux/1/svcs>.

- Listează toate serviciile care rulează:

`svcs`

- Listează serviciile care nu rulează:

`svcs -vx`

- Listează informații despre un serviciu:

`svcs apache`

- Afișează locația fișierului de jurnal al unui serviciu:

`svcs -L apache`

- Afișează finalul fișierului de jurnal al unui serviciu:

`tail $(svcs -L apache)`
