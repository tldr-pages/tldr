# docker rmi

> Eliminați una sau mai multe imagini Docker.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/rmi/>

- Arată ajutor:

`docker rmi`

- Eliminați una sau mai multe imagini date numele lor:

`docker rmi {{image1 image2 ...}}`

- Forța elimina o imagine:

`docker rmi --force {{image}}`

- Eliminați o imagine fără a șterge părinții fără taguri:

`docker rmi --no-prune {{image}}`
