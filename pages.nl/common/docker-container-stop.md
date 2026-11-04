# docker container stop

> Stop één of meer draaiende containers.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/container/stop/>.

- Stop een Docker-container:

`docker {{[stop|container stop]}} {{container}}`

- Stop een container en stuur er een specifiek signaal naartoe:

`docker {{[stop|container stop]}} {{[-s|--signal]}} {{signal}} {{container}}`

- Stop een container en wacht een specifiek aantal seconden voordat deze geforceerd wordt beëindigd:

`docker {{[stop|container stop]}} {{[-t|--timeout]}} {{seconden}} {{container}}`

- Stop één of meer containers:

`docker {{[stop|container stop]}} {{container1 container2 ...}}`

- Toon de help:

`docker {{[stop|container stop]}} --help`
