# docker images

> Gestionare imagini Docker.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/images/>

- Listează toate imaginile Docker:

`docker images`

- Listează toate imaginile Docker, inclusiv intermediarii:

`docker images --all`

- Listează ieșirea în modul silențios (numai ID-uri numerice):

`docker images --quiet`

- Listează toate imaginile Docker care nu sunt utilizate de niciun container:

`docker images --filter dangling=true`

- Listează imaginile care conțin un substring în numele lor:

`docker images "{{*name*}}"`
