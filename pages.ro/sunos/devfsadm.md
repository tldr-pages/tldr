# devfsadm

> Comandă de administrare pentru `/dev`.
> Menține spațiul de nume `/dev`.
> Mai multe informații: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Scanează după discuri noi:

`devfsadm -c disk`

- Curăță orice legături (links) `/dev` invalide și scanează după dispozitive noi:

`devfsadm -C -v`

- Simulare - afișează ce s-ar schimba, dar nu efectuează nicio modificare:

`devfsadm -C -v -n`