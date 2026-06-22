# apptainer shell

> Avvia una shell interattiva all'interno di un container Apptainer.
> Vedi anche: `apptainer exec`, `apptainer run`.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_shell.html>.

- Avvia una shell interattiva all'interno di un container:

`apptainer shell {{path/to/immagine.sif}}`

- Avvia una shell con un mount bind dall'host al container:

`apptainer shell {{[-B|--bind]}} {{path/to/source}}:{{path/to/destinazione}} {{path/to/immagine.sif}}`

- Avvia una shell con variabili d'ambiente:

`apptainer shell --env {{variabile}}={{valore}} {{path/to/immagine.sif}}`

- Avvia una shell in modalità completamente isolata (filesystem, PID, IPC e ambiente pulito):

`apptainer shell {{[-C|--containall]}} {{path/to/immagine.sif}}`

- Avvia una shell con un overlay del filesystem temporaneo scrivibile:

`apptainer shell --writable-tmpfs {{path/to/immagine.sif}}`

- Avvia una shell con supporto GPU NVIDIA:

`apptainer shell --nv {{path/to/immagine.sif}}`

- Avvia una shell utilizzando un programma shell specifico:

`apptainer shell {{[-s|--shell]}} {{path/to/shell}} {{path/to/immagine.sif}}`

- Mostra aiuto:

`apptainer shell {{[-h|--help]}}`
