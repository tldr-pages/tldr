# docker-machine

> Dockert futtató gépek létrehozása és kezelése. További információ: <https://docs.docker.com/machine/reference/>.

- A jelenleg futó docker gépek listázása:

`docker-machine ls`

- Új docker gép létrehozása adott névvel:

`docker-machine create {{name}}`

- Egy gép állapotának lekérdezése:

`docker-machine status {{name}}`

- Egy gép indítása:

`docker-machine start {{name}}`

- Egy gép leállítása:

`docker-machine stop {{name}}`

- Információk megtekintése egy gépről:

`docker-machine inspect {{name}}`
