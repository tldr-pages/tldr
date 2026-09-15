# chmod

> Cambia i permessi di accesso di file o directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html>.

- Dai al proprietario di un file il permesso di e[x]ecute:

`chmod u+x {{percorso/del/file}}`

- Dai al proprietario i permessi di [r]ead e [w]rite su un file/directory:

`chmod u+rw {{percorso/del/file_o_directory}}`

- Rimuovi i permessi di e[x]ecute dal [g]ruppo:

`chmod g-x {{percorso/del/file}}`

- Dai a tutti gli utenti i permessi di [r]ead e e[x]ecute:

`chmod a+rx {{percorso/del/file}}`

- Dai ad altri utenti (non nel gruppo proprietario del file) gli stessi diritti del [g]ruppo:

`chmod o=g {{percorso/del/file}}`

- Rimuovi tutti i permessi per gli altri:

`chmod o= {{percorso/del/file}}`

- Cambia i permessi ricorsivamente dando al [g]ruppo e agli [o]ttri la possibilità di [w]rite:

`chmod {{[-R|--recursive]}} g+w,o+w {{percorso/della/directory}}`

- Ricorsivamente dà a tutti gli utenti i permessi di [r]ead sui file. Dà anche i permessi di e[X]ecute ai file che hanno almeno un permesso di esecuzione e a tutte le sottodirectory:

`chmod {{[-R|--recursive]}} a+rX {{percorso/della/directory}}`
