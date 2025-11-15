# autojump

> Salta velocemente tra le directory che usi più spesso.
> Alias come `j` o `jc` sono disponibili per una maggiore velocità di scrittura.
> Maggiori informazioni: <https://github.com/wting/autojump>.

- Muoviti in una directory il cui nome contiene una parola chiave:

`j {{parola_chiave}}`

- Salta in una sotto-directory della directory corrente il quale nome contiene una parola chiave:

`jc {{parola_chiave}}`

- Apri una directory il cui nome contiene una parola chiave nel gestore file di sistema:

`jo {{parola_chiave}}`

- Rimuovi directory non esistenti dal database di `autojump`:

`j --purge`

- Mostra le voci nel database di `autojump`:

`j {{[-s|--stat]}}`
