# chroot

> Esegui un comando o una shell interattiva con una speciale directory root.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- Esegui `$SHELL` nella nuova directory root:

`sudo chroot {{percorso/della/nuova/root}}`

- Esegui un comando nella nuova directory root:

`sudo chroot {{percorso/della/nuova/root}} {{comando}}`

- Usa un utente e un gruppo specifici:

`sudo chroot --userspec {{nome_utente_o_id}}:{{nome_gruppo_o_id}} {{percorso/della/nuova/root}}`
