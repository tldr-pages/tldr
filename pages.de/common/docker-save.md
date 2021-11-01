# docker save

> Exportiere eines oder mehrere Docker Images in ein Archiv.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/save/>.

- Speichere ein Image über die Standardausgabe in ein Tar-Archiv:

`docker save {{image}}:{{tag}} > {{pfad/zur/datei.tar}}`

- Speichere ein Image in ein Tar-Archiv:

`docker save --output {{pfad/zur/datei.tar}} {{image}}:{{tag}}`

- Speichere alle Tags eines Images:

`docker save --output {{pfad/zur/datei.tar}} {{image_name}}`

- Speichere nur bestimmte Tags eines Images:

`docker save --output {{pfad/zur/datei.tar}} {{image_name:tag1 image_name:tag2 ...}}`
