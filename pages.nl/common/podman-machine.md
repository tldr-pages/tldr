# podman machine

> Maak virtuele machines aan waarop Podman draait en beheer deze.
> Inbegrepen vanaf Podman versie 4.
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-machine.1.html>.

- Toon bestaande machines:

`podman machine {{[ls|list]}}`

- Maak een nieuwe standaardmachine aan:

`podman machine init`

- Maak een nieuwe machine aan met een specifieke naam:

`podman machine init {{naam}}`

- Maak een nieuwe machine aan met andere resources:

`podman machine init --cpus {{4}} --memory {{4096}} --disk-size {{50}}`

- Start of stop een machine:

`podman machine {{start|stop}} {{naam}}`

- Maak verbinding met een draaiende machine via SSH:

`podman machine ssh {{naam}}`

- Bekijk informatie over een machine:

`podman machine inspect {{naam}}`
