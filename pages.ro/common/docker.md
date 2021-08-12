# docker

> Gestionați containerele și imaginile Docker.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/cli/>

- Lista containerelor de andocare rulează în prezent:

`docker ps`

- Listează toate containerele de andocare (rulează și oprit):

`docker ps -a`

- Porniți un container dintr-o imagine, cu un nume personalizat:

`docker run --name {{container_name}} {{image}}`

- Porniți sau opriți un container existent:

`docker {{start|stop}} {{container_name}}`

- Trageți o imagine dintr-un registru de andocare:

`docker pull {{image}}`

- Deschideți un înveliș în interiorul unui container deja rulat:

`docker exec -it {{container_name}} {{sh}}`

- Scoateţi un recipient oprit:

`docker rm {{container_name}}`

- Adu și urmați jurnalele unui container:

`docker logs -f {{container_name}}`
