# docker-machine

> Creați și gestionați utilaje care rulează Docker.
> Mai multe informaţii: <https://docs.docker.com/machine/reference/>

- Lista care rulează în prezent mașini de andocare:

`docker-machine ls`

- Creați o nouă mașină de docher cu un nume specific:

`docker-machine create {{name}}`

- Obțineți statutul unei mașini:

`docker-machine status {{name}}`

- Porneşte o maşină:

`docker-machine start {{name}}`

- Opreşte o maşină.

`docker-machine stop {{name}}`

- Inspectați informațiile despre o mașină:

`docker-machine inspect {{name}}`
