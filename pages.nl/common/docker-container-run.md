# docker container run

> Voer een commando uit in een nieuwe Docker-container.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/container/run/>.

- Voer een commando uit in een nieuwe container vanuit een getagd image:

`docker {{[run|container run]}} {{image:tag}} {{commando}}`

- Voer een commando uit in een nieuwe container op de achtergrond en toon de ID ervan:

`docker {{[run|container run]}} {{[-d|--detach]}} {{image}} {{commando}}`

- Voer een commando uit in een eenmalige container in interactieve modus en pseudo-TTY:

`docker {{[run|container run]}} --rm {{[-it|--interactive --tty]}} {{image}} {{commando}}`

- Voer een commando uit in een nieuwe container met doorgegeven omgevingsvariabelen:

`docker {{[run|container run]}} {{[-e|--env]}} '{{variable}}={{value}}' {{[-e|--env]}} {{variable}} {{image}} {{commando}}`

- Voer een commando uit in een nieuwe container met gebonden volumes:

`docker {{[run|container run]}} {{[-v|--volume]}} /{{path/to/host_path}}:/{{path/to/container_path}} {{image}} {{commando}}`

- Voer een commando uit in een nieuwe container met gepubliceerde poorten:

`docker {{[run|container run]}} {{[-p|--publish]}} {{host_port}}:{{container_port}} {{image}} {{commando}}`

- Voer een commando uit in een nieuwe container en overschrijf het beginpunt van de image:

`docker {{[run|container run]}} --entrypoint {{commando}} {{image}}`

- Voer een commando uit in een nieuwe container die deze verbindt met een netwerk:

`docker {{[run|container run]}} --network {{netwerk}} {{image}}`
