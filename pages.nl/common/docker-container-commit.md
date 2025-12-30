# docker container commit

> Maak een nieuw image van de wijzigingen van een container.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/container/commit/>.

- Maak een image van een specifieke container:

`docker {{[commit|container commit]}} {{container}} {{image}}:{{tag}}`

- Pas een `CMD` Dockerfile instructie toe op de aangemaakte image:

`docker {{[commit|container commit]}} {{[-c|--change]}} "CMD {{commando}}" {{container}} {{image}}:{{tag}}`

- Pas een `ENV` Dockerfile-instructie toe op de aangemaakte image:

`docker {{[commit|container commit]}} {{[-c|--change]}} "ENV {{naam}}={{waarde}}" {{container}} {{image}}:{{tag}}`

- Maak een afbeelding met een specifieke auteur in de metadata:

`docker {{[commit|container commit]}} {{[-a|--author]}} "{{author}}" {{container}} {{image}}:{{tag}}`

- Maak een afbeelding met een specifieke opmerking in de metagegevens:

`docker {{[commit|container commit]}} {{[-m|--message]}} "{{comment}}" {{container}} {{image}}:{{tag}}`

- Maak een image zonder de container te pauzeren tijdens het vastleggen:

`docker {{[commit|container commit]}} {{[-p|--pause]}} false {{container}} {{image}}:{{tag}}`

- Toon de help:

`docker {{[commit|container commit]}} --help`
