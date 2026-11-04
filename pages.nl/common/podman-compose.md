# podman-compose

> Voer een Compose Specification container-definitie uit en beheer deze.
> Meer informatie: <https://github.com/containers/podman-compose>.

- Toon alle draaiende containers:

`podman-compose ps`

- Maak alle containers aan en start ze op de achtergrond met een lokaal `docker-compose.yml`:

`podman-compose up {{[-d|--detach]}}`

- Start alle containers, en bouw deze indien nodig:

`podman-compose up --build`

- Start alle containers met een alternatief compose-bestand:

`podman-compose {{[-f|--file]}} {{pad/naar/bestand.yaml}} up`

- Stop alle draaiende containers:

`podman-compose stop`

- Verwijder alle containers, netwerken en volumes:

`podman-compose down {{[-v|--volumes]}}`

- Volg de logs van een container (laat alle containernamen weg):

`podman-compose logs {{[-f|--follow]}} {{container_naam}}`

- Voer een eenmalig commando uit in een service zonder gekoppelde poorten:

`podman-compose run {{service_naam}} {{commando}}`
