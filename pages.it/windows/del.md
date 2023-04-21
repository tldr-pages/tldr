# del

> Cancella uno o più file.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Cancella uno o più (separati da uno spazio) file o pattern:

`del {{pattern_di_file}}`

- Chiedi conferma prima di cancellare ogni file:

`del {{pattern_di_file}} /p`

- Forza l'eliminazione di un file a sola lettura:

`del {{pattern_di_file}} /f`

- Elimina in modo ricorsivo i file da tutte le sottodirectory:

`del {{pattern_di_file}} /s`

- Non chiedere conferma quando si eliminano i file in base a un carattere globale:

`del {{pattern_di_file}} /q`

- Mostra il messaggio d'aiuto e fà vedere la lista di attributi disponibili:

`del /?`

- Cancella dei file in base a degli attributi specifici:

`del {{pattern_di_file}} /a {{attributo}}`
