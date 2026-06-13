# docker image save

> Exporteer Docker-images naar archief.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/image/save/>.

- Sla een image op door `stdout` om te leiden naar een `.tar` archief:

`docker {{[save|image save]}} {{image}}:{{tag}} > {{pad/naar/bestand.tar}}`

- Sla een image op in een `.tar` archief:

`docker {{[save|image save]}} {{[-o|--output]}} {{pad/naar/bestand.tar}} {{image}}:{{tag}}`

- Sla alle tags van het image op:

`docker {{[save|image save]}} {{[-o|--output]}} {{pad/naar/bestand.tar}} {{image_naam}}`

- Kies bepaalde tags van een image om op te slaan:

`docker {{[save|image save]}} {{[-o|--output]}} {{pad/naar/bestand.tar}} {{image_naam:tag1 image_naam:tag2 ...}}`
