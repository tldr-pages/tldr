# podman run

> Voer een commando uit in een nieuwe Podman-container.
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-run.1.html>.

- Voer een commando uit in een nieuwe container op basis van een getagde image:

`podman run {{image:tag}} {{commando}}`

- Voer een commando uit in een nieuwe container op de achtergrond en toon de ID ervan:

`podman run {{[-d|--detach]}} {{image:tag}} {{commando}}`

- Voer een commando uit in een eenmalige container in interactieve modus en pseudo-tty:

`podman run --rm {{[-it|--interactive --tty]}} {{image:tag}} {{commando}}`

- Voer een commando uit in een nieuwe container met doorgegeven omgevingsvariabelen:

`podman run {{[-e|--env]}} '{{variabele}}={{waarde}}' {{[-e|--env]}} {{variabele}} {{image:tag}} {{commando}}`

- Voer een commando uit in een nieuwe container met gebonden volumes:

`podman run {{[-v|--volume]}} /{{pad/naar/hostpad}}:/{{pad/naar/containerpad}} {{image:tag}} {{commando}}`

- Voer een commando uit in een nieuwe container met gepubliceerde poorten:

`podman run {{[-p|--publish]}} {{hostpoort}}:{{containerpoort}} {{image:tag}} {{commando}}`

- Voer een commando uit in een nieuwe container waarbij het entrypoint van de image wordt overschreven:

`podman run --entrypoint {{commando}} {{image:tag}}`

- Voer een commando uit in een nieuwe container en verbind deze met een netwerk:

`podman run --network {{netwerk}} {{image:tag}}`
