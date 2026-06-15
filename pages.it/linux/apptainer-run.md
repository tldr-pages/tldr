# apptainer run

> Esegue lo script di avvio predefinito di un container Apptainer.
> Lo script di avvio è definito nella sezione `%runscript` del file di definizione del container.
> Vedi anche: `apptainer exec`, `apptainer shell`.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_run.html>.

- Esegue lo script di avvio predefinito di un container:

`apptainer run {{path/to/immagine.sif}}`

- Esegue con argomenti passati allo script di avvio:

`apptainer run {{path/to/immagine.sif}} {{arg1 arg2 ...}}`

- Esegue con un mount bind dall'host al container:

`apptainer run {{[-B|--bind]}} {{path/to/source}}:{{path/to/destinazione}} {{path/to/immagine.sif}}`

- Esegue con variabili d'ambiente:

`apptainer run --env {{variabile}}={{valore}} {{path/to/immagine.sif}}`

- Esegue in modalità completamente isolata (filesystem, PID, IPC e ambiente pulito):

`apptainer run {{[-C|--containall]}} {{path/to/immagine.sif}}`

- Esegue con un overlay del filesystem temporaneo scrivibile:

`apptainer run --writable-tmpfs {{path/to/immagine.sif}}`

- Esegue con supporto GPU NVIDIA:

`apptainer run --nv {{path/to/immagine.sif}}`

- Mostra aiuto:

`apptainer run {{[-h|--help]}}`
