# docker run

> Egy parancs futtatása egy új Docker konténerben. További információ: <https://docs.docker.com/engine/reference/commandline/run/>.

- Parancs futtatása egy új konténerben egy megjelölt képből:

`docker run {{image:tag}} {{command}}`

- Parancs futtatása egy új konténerben a háttérben, és annak azonosítójának megjelenítése:

`docker run --detach {{image}} {{command}}`

- Parancs futtatása egy új konténerben interaktív módban és pszeudo-TTY-ben:

`docker run --rm --interactive --tty {{image}} {{command}}`

- Parancs futtatása egy új konténerben átadott környezeti változókkal:

`docker run --env '{{variable}}={{value}}' --env {{variable}} {{image}} {{command}}`

- Parancs futtatása egy új konténerben kötött csatlakoztatott kötetekkel:

`docker run --volume {{/path/to/host_path}}:{{/path/to/container_path}} {{image}} {{command}}`

- Parancs futtatása egy új konténerben közzétett portokkal:

`docker run --publish {{host_port}}:{{container_port}} {{image}} {{command}}`

- Parancs futtatása egy új konténerben a kép belépési pontjának felülírása:

`docker run --entrypoint {{command}} {{image}}`

- Parancs futtatása egy új konténerben, amely hálózathoz csatlakozik:

`docker run --network {{network}} {{image}}`
