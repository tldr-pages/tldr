# docker exec

> Esegui un comando su un Docker container in esecuzione.
> Maggiori informazioni: <https://docs.docker.com/reference/cli/docker/container/exec/>.

- Avvia una shell interattiva all'interno di un container in esecuzione:

`docker exec {{[-it|--interactive --tty]}} {{nome_container}} {{/bin/bash}}`

- Esegui un commando in background ("detached") su un container in esecuzione:

`docker exec {{[-d|--detach]}} {{nome_container}} {{comando}}`

- Seleziona la directory di lavoro in cui eseguire un dato comando:

`docker exec {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{percorso/della/directory}} {{nome_container}} {{comando}}`

- Esegui un comando in background su un container esistente, mantenendo aperto `stdin`:

`docker exec {{[-i|--interactive]}} {{[-d|--detach]}} {{nome_container}} {{comando}}`

- Imposta una variabile d'ambiente in una sessione Bash in esecuzione:

`docker exec {{[-it|--interactive --tty]}} {{[-e|--env]}} {{nome_variabile}}={{valore}} {{nome_container}} {{/bin/bash}}`

- Specifica l'utente da usare per eseguire un comando:

`docker exec {{[-u|--user]}} {{utente}} {{nome_container}} {{comando}}`
