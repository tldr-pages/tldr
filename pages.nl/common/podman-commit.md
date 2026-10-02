# podman commit

> Maak een nieuwe image op basis van de gewijzigde container.
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-commit.1.html>.

- Maak een image van een specifieke container:

`podman commit {{container}} {{image}}:{{tag}}`

- Pas een `ENV`-instructie toe op de aangemaakte image:

`podman commit {{[-c|--change]}} "ENV {{naam}}={{waarde}}" {{container}} {{image}}:{{tag}}`

- Pas `LABEL`-, `ENTRYPOINT`- en `CMD`-instructies toe op de aangemaakte image:

`podman commit {{[-c|--change]}} CMD={{commando}} {{[-c|--change]}} ENTRYPOINT={{commando}} {{[-c|--change]}} "LABEL {{sleutel}}={{waarde}}" {{container}} {{image}}:{{tag}}`

- Maak een image met een specifieke auteur en opmerking in de metadata:

`podman commit {{[-a|--author]}} "{{auteur}}" {{[-m|--message]}} "{{opmerking}}" {{container}} {{image}}:{{tag}}`

- Maak een image zonder de container te pauzeren tijdens het committen:

`podman commit {{[-p|--pause]}} false {{container}} {{image}}:{{tag}}`

- Toon de help:

`podman commit --help`
