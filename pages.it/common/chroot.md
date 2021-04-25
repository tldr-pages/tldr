# chroot

> Esegui un comando o una shell interattiva con una speciale root directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/chroot>.

- Esegui un comando con una diversa root directory:

`chroot {{/percorso/alla/nuova/root}} {{comando}}`

- Specifica utente e gruppo (ID o nome) da usare:

`chroot --userspec={{utente:gruppo}}`
