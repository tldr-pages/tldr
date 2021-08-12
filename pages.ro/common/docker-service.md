# docker service

> Gestionați serviciile pe un demonon de andocare.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/service/>

- Lista serviciilor pe un daemon docher:

`docker service ls`

- Creați un serviciu nou:

`docker service create --name {{service_name}} {{image}}:{{tag}}`

- Afișarea informațiilor detaliate privind o listă de servicii separate prin spațiu:

`docker service inspect {{service_name|ID}}`

- Listați sarcinile unei liste de servicii separate prin spațiu:

`docker service ps {{service_name|ID}}`

- Scalați la un anumit număr de replici pentru o listă de servicii separate de spațiu:

`docker service scale {{service_name}}={{count_of_replicas}}`

- Eliminați o listă de servicii separate de spațiu:

`docker service rm {{service_name|ID}}`
