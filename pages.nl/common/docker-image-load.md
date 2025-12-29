# docker image load

> Laad Docker-images vanuit bestanden of `stdin`.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/image/load/>.

- Laad een Docker-image vanuit `stdin`:

`docker < {{path/naar/image_bestand.tar}} {{[load|image load]}}`

- Laad een Docker image vanuit een specifiek bestand:

`docker {{[load|image load]}} {{[-i|--input]}} {{pad/naar/image_bestand.tar}}`

- Laad een Docker image vanuit een specifiek bestand in stille modus:

`docker {{[load|image load]}} {{[-q|--quiet]}} {{[-i|--input]}} {{pad/naar/image_bestand.tar}}`
