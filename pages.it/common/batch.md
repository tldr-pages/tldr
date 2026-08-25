# batch

> Esegue comandi in un momento successivo quando i livelli di carico del sistema lo permettono.
> I risultati vengono inviati alla mail dell'utente.
> Vedi anche: `at`, `atq`, `atrm`, `mail`.
> Maggiori informazioni: <https://manned.org/batch>.

- Esegue comandi da `stdin` (premi `<Ctrl d>` quando finito):

`batch`

- Esegue un comando da `stdin`:

`echo "{{./make_db_backup.sh}}" | batch`
