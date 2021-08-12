# docker network

> Creați și gestionați rețele de andocare.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/network/>

- Listează toate rețelele disponibile și configurate pe daemon docker:

`docker network ls`

- Crearea unei rețele definite de utilizator:

`docker network create --driver {{driver_name}} {{network_name}}`

- Afișează informații detaliate despre o listă de rețele separate în spațiu:

`docker network inspect {{network_name}}`

- Conectați un container la o rețea utilizând un nume sau un ID:

`docker network connect {{network_name}} {{container_name|ID}}`

- Deconectați un container de la o rețea:

`docker network disconnect {{network_name}} {{container_name|ID}}`

- Eliminați toate rețelele neutilizate (care nu se referă la niciun container):

`docker network prune`

- Eliminați o listă separată de rețele neutilizate:

`docker network rm {{network_name}}`
