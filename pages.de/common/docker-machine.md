# docker-machine

> Erstelle und verwalte Maschinen, die Docker ausführen.
> Weitere Informationen: <https://docs.docker.com/machine/reference/>.

- Liste zur Zeit laufende Docker Maschinen auf:

`docker-machine ls`

- Erzeuge eine neue Docker Maschine mit einem spezifischen Namen:

`docker-machine create {{name}}`

- Zeige den Status einer Maschine:

`docker-machine status {{name}}`

- Starte eine Maschine:

`docker-machine start {{name}}`

- Stoppe eine Maschine:

`docker-machine stop {{name}}`

- Zeige Informationen über eine Maschine:

`docker-machine inspect {{name}}`
