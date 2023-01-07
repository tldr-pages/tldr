# chroot

> Esegui un comando o una shell interattiva con una speciale directory root.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/chroot>.

- Esegui un comando con una diversa directory root:

`chroot {{/percorso/della/nuova/root}} {{comando}}`

- Specifica utente e gruppo (ID o nome) da usare:

`chroot --userspec={{utente:gruppo}}`
