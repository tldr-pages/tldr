# docker container

> Verwalte Docker Container.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/container/>.

- Liste zur Zeit laufende Container auf:

`docker {{[ps|container ls]}}`

- Starte einen oder mehrere gestoppte Container:

`docker {{[start|container start]}} {{container1_name}} {{container2_name}}`

- Beende einen oder mehrere laufende Container sofort:

`docker {{[kill|container kill]}} {{container_name}}`

- Stoppe einen oder mehrere laufende Container:

`docker {{[stop|container stop]}} {{container_name}}`

- Pausiere alle Prozesse in einem oder mehreren Containern:

`docker {{[pause|container pause]}} {{container_name}}`

- Zeige detaillierte Informationen zu einem oder mehreren Containern an:

`docker container inspect {{container_name}}`

- Exportiere das Dateisystem eines Containers als `.tar` Archiv:

`docker {{[export|container export]}} {{container_name}}`

- Erstelle ein neues Image aus den Änderungen eines Containers:

`docker {{[commit|container commit]}} {{container_name}}`
