# docker logs

> Zeige Container Logs.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Zeige die Logs eines Containers:

`docker logs {{container_name}}`

- Zeige die Logs und aktualisiere sie automatisch:

`docker logs {{[-f|--follow]}} {{container_name}}`

- Zeige die letzten 5 Zeilen:

`docker logs {{container_name}} {{[-n|--tail]}} {{5}}`

- Zeige die Logs und füge ihnen Zeitstempel hinzu:

`docker logs {{[-t|--timestamps]}} {{container_name}}`

- Zeige Logs vor einem bestimmten Zeitpunkt der Ausführung des Containers (bspw. 23m, 10s, 2013-01-02T13:23:37):

`docker logs {{container_name}} --until {{time}}`
