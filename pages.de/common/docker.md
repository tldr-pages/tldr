# docker

> Verwalte Docker Container und Images.
> Manche Unterbefehle wie `run` sind separat dokumentiert.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/>.

- Liste laufende und gestoppte Container auf:

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Erzeuge einen Container aus einem Image und benenne ihn:

`docker {{[run|container run]}} --name {{container_name}} {{image}}`

- Stoppe oder starte einen existierenden Container:

`docker container {{start|stop}} {{container_name}}`

- Lade ein Image herunter:

`docker {{[pull|image pull]}} {{image}}`

- Zeige eine Liste der bereits heruntergeladenen Images an:

`docker {{[images|image ls]}}`

- Öffne eine Konsole innerhalb eines bereits laufenden Containers:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{container_name}} {{sh}}`

- Lösche einen gestoppten Container:

`docker {{[rm|container rm]}} {{container_name}}`

- Zeige die Logs eines Containers an und aktualisiere sie automatisch:

`docker {{[logs|container logs]}} {{[-f|--follow]}} {{container_name}}`
