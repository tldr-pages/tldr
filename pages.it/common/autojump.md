# autojump

> Salta velocemente tra le directory che visiti più spesso.
> Alias come `j` o `jc` sono disponibili per una digitazione ancora più veloce.
> Vedi anche: `bashmarks`.
> Maggiori informazioni: <https://github.com/wting/autojump#name>.

- Aggiungi gli alias `autojump` al tuo shell:

`source /usr/share/autojump/autojump.{{bash|fish|zsh}}`

- Salta in una directory che contiene il pattern specificato:

`j {{pattern}}`

- Salta in una sotto-directory (figlia) della directory corrente che contiene il pattern specificato:

`jc {{pattern}}`

- Apri una directory che contiene il pattern specificato nel gestore file del sistema operativo:

`jo {{pattern}}`

- Rimuovi le directory non esistenti dal database di `autojump`:

`j --purge`

- Mostra le voci nel database di `autojump`:

`j -s`
