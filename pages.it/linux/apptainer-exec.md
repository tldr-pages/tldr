# apptainer exec

> Esegue un comando all'interno di un container Apptainer.
> Vedi anche: `apptainer run`, `apptainer shell`.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_exec.html>.

- Esegue un comando all'interno di un container:

`apptainer exec {{path/to/immagine.sif}} {{comando}}`

- Esegue un comando con argomenti:

`apptainer exec {{path/to/immagine.sif}} {{comando}} {{arg1 arg2 ...}}`

- Esegue un comando con un mount bind dall'host al container:

`apptainer exec {{[-B|--bind]}} {{path/to/source}}:{{path/to/destinazione}} {{path/to/immagine.sif}} {{comando}}`

- Esegue un comando con variabili d'ambiente:

`apptainer exec --env {{variabile}}={{valore}} {{path/to/immagine.sif}} {{comando}}`

- Esegue un comando in modalità completamente isolata (filesystem, PID, IPC e ambiente pulito):

`apptainer exec {{[-C|--containall]}} {{path/to/immagine.sif}} {{comando}}`

- Esegue un comando con un overlay del filesystem temporaneo scrivibile:

`apptainer exec --writable-tmpfs {{path/to/immagine.sif}} {{comando}}`

- Esegue un comando con supporto GPU NVIDIA:

`apptainer exec --nv {{path/to/immagine.sif}} {{comando}}`

- Mostra aiuto:

`apptainer exec {{[-h|--help]}}`
