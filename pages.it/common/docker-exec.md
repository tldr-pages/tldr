# docker exec

> Esegui un comando su un Docker container in esecuzione.
> Maggiori informazioni: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Avvia una shell interattiva all'interno di un container in esecuzione:

`docker exec --interactive --tty {{nome_container}} {{/bin/bash}}`

- Esegui un commando in background ("detached") su un container in esecuzione:

`docker exec --detach {{nome_container}} {{comando}}`

- Seleziona la directory di lavoro in cui eseguire un dato comando:

`docker exec --interactive -tty --workdir {{percorso/della/directory}} {{nome_container}} {{comando}}`

- Esegui un comando in background su un container esistente, mantenendo aperto `stdin`:

`docker exec --interactive --detach {{nome_container}} {{comando}}`

- Imposta una variabile d'ambiente in una sessione bash in esecuzione:

`docker exec --interactive --tty --env {{nome_variabile}}={{valore}} {{nome_container}} {{/bin/bash}}`

- Specifica l'utente da usare per eseguire un comando:

`docker exec --user {{utente}} {{nome_container}} {{comando}}`
