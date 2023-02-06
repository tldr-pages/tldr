# podman machine

> Virtuális gépek létrehozása és kezelése Podman futtatásával. A Podman 4-es vagy nagyobb verziójához tartozik. További információ: <https://docs.podman.io/en/latest/markdown/podman-machine.1.html>.

- Meglévő gépek listázása:

`podman machine ls`

- Új alapértelmezett gép létrehozása:

`podman machine init`

- Új gép létrehozása egy adott névvel:

`podman machine init {{name}}`

- Új gép létrehozása különböző erőforrásokkal:

`podman machine init --cpus={{4}} --memory={{4096}} --disk-size={{50}}`

- Egy gép indítása vagy leállítása:

`podman machine {{start|stop}} {{name}}`

- Csatlakozás egy futó géphez SSH-n keresztül:

`podman machine ssh {{name}}`

- Információk megtekintése egy gépről:

`podman machine inspect {{name}}`
