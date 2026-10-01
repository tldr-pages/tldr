# podman

> Eenvoudig beheertool voor pods, containers en images.
> Biedt een met Docker-CLI vergelijkbare command-line. Simpel gezegd: `alias docker=podman`.
> Meer informatie: <https://docs.podman.io/en/latest/Commands.html>.

- Toon alle containers (actief en gestopt):

`podman ps {{[-a|--all]}}`

- Maak een container aan van een image, met een aangepaste naam:

`podman run --name {{container_naam}} {{image}}`

- Start of stop een bestaande container:

`podman {{start|stop}} {{container_naam}}`

- Download een image uit een register (standaard Docker Hub):

`podman pull {{image}}`

- Toon de lijst van reeds gedownloade images:

`podman images`

- Open een shell binnen een reeds draaiende container:

`podman exec {{[-it|--interactive --tty]}} {{container_naam}} {{sh}}`

- Verwijder een gestopte container:

`podman rm {{container_naam}}`

- Toon de logs van een of meer containers en volg de log-uitvoer:

`podman logs {{[-f|--follow]}} {{container_naam_of_id1 container_naam_of_id2 ...}}`
