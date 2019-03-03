# chmod

> Cambia i permessi di accesso di file o directory.

- Dai il permesso di eseguire (x) un file al suo proprietario (u):

`chmod u+x {{percorso/al/file}}`

- Dai permessi di lettura (r) e scrittura (w) per un file/directory al suo proprietario:

`chmod u+rw {{percorso/a/file_o_directory}}`

- Rimuovi i permessi di esecuzione al [g]ruppo proprietario del file:

`chmod g-x {{percorso/al/file}}`

- Dai a tutti gli utenti (a) diritti di lettura ed esecuzione:

`chmod a+rx {{percorso/al/file}}`

- Dai ad altri utenti (non nel gruppo proprietario) gli stessi diritti del gruppo:

`chmod o=g {{percorso/al/file}}`

- Cambia permessi ricorsivamente dando al [g]ruppo e agli altri utenti (o) diritto di scrittura:

`chmod -R g+w,o+w {{percorso/alla/directory}}`
