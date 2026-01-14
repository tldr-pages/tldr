# docker container exec

> Voer een opdracht uit op een Docker-container die al draait.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/container/exec/>.

- Start een interactieve shellsessie op een reeds draaiende container:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{container_naam}} {{/bin/bash}}`

- Voer een commando uit op de achtergrond (detached) op een draaiende container:

`docker {{[exec|container exec]}} {{[-d|--detach]}} {{container_naam}} {{commando}}`

- Selecteer de werkmap waarin een gegeven commando moet worden uitgevoerd:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{pad/naar/map}} {{container_naam}} {{commando}}`

- Voer een opdracht op de achtergrond uit op een bestaande container, maar houd `stdin` open:

`docker {{[exec|container exec]}} {{[-i|--interactive]}} {{[-d|--detach]}} {{container_naam}} {{commando}}`

- Stel een omgevingsvariabele in in een lopende Bash-sessie:

`docker {{[exec|container exec]}} {{[-it|--interactive --tty]}} {{[-e|--env]}} {{variabele_naam}}={{waarde}} {{container_name}} {{/bin/bash}}`

- Voer een opdracht uit als een specifieke gebruiker:

`docker {{[exec|container exec]}} {{[-u|--user]}} {{gebruiker}} {{container_naam}} {{commando}}`
