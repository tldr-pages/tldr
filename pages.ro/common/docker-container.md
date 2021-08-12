# docker container

> Gestionaţi containerele Docker.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/container/>

- Lista containerelor Docker care rulează în prezent:

`docker container ls`

- Porniți unul sau mai multe containere oprite:

`docker container start {{container1_name}} {{container2_name}}`

- Ucide unul sau mai multe containere care rulează:

`docker container kill {{container_name}}`

- Opriți unul sau mai multe containere de funcționare:

`docker container stop {{container_name}}`

- Întrerupeți toate procesele din interiorul unuia sau mai multor containere:

`docker container pause {{container_name}}`

- Afișați informații detaliate pe unul sau mai multe containere:

`docker container inspect {{container_name}}`

- Exportați sistemul de fișiere al unui container ca arhivă de gudron:

`docker container export {{container_name}}`

- Creați o imagine nouă din modificările unui container:

`docker container commit {{container_name}}`
