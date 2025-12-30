# docker container update

> Configuratie van Docker-containers updaten.
> Opmerking: dit commando wordt niet ondersteund voor Windows-containers.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/container/update/>.

- Update het herstartbeleid om toe te passen wanneer een specifieke container wordt afgesloten:

`docker {{[update|container update]}} --restart {{always|no|on-failure|unless-stopped}} {{container_naam}}`

- Update het beleid om een specifieke container tot drie keer toe opnieuw te starten als deze afsluit met een exit-status van niet nul:

`docker {{[update|container update]}} --restart on-failure:3 {{container_naam}}`

- Update het aantal CPU's dat beschikbaar is voor een specifieke container:

`docker {{[update|container update]}} --cpus {{aantal}} {{container_naam}}`

- Update het geheugenlimiet in [M]egabytes voor een specifieke container:

`docker {{[update|container update]}} {{[-m|--memory]}} {{limiet}}M {{container_naam}}`

- Update het maximum aantal proces-ID's dat is toegestaan in een specifieke container (gebruik `-1` voor onbeperkt):

`docker {{[update|container update]}} --pids-limit {{aantal}} {{container_naam}}`

- Update de hoeveelheid geheugen in [M]egabytes die een specifieke container naar schijf mag swappen (gebruik `-1` voor onbeperkt):

`docker {{[update|container update]}} --memory-swap {{limiet}}M {{container_naam}}`
