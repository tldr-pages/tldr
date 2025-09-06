# docker save

> Exportiere eines oder mehrere Docker Images in ein Archiv.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/image/save/>.

- Speichere ein Image über die Standardausgabe in ein Tar-Archiv:

`docker save {{image}}:{{tag}} > {{pfad/zu/datei.tar}}`

- Speichere ein Image in ein Tar-Archiv:

`docker save {{[-o|--output]}} {{pfad/zu/datei.tar}} {{image}}:{{tag}}`

- Speichere alle Tags eines Images:

`docker save {{[-o|--output]}} {{pfad/zu/datei.tar}} {{image_name}}`

- Speichere nur bestimmte Tags eines Images:

`docker save {{[-o|--output]}} {{pfad/zu/datei.tar}} {{image_name:tag1 image_name:tag2 ...}}`
