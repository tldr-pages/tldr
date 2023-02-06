# docker save

> Egy vagy több dokkoló kép exportálása archívumba. További információ: <https://docs.docker.com/engine/reference/commandline/save/>.

- Egy kép mentése a `stdout` átirányításával egy tar archívumba:

`docker save {{image}}:{{tag}} > {{path/to/file.tar}}`

- Egy kép mentése tar archívumba:

`docker save --output {{path/to/file.tar}} {{image}}:{{tag}}`

- A kép összes címkéjének mentése:

`docker save --output {{path/to/file.tar}} {{image_name}}`

- A kép egyes címkéinek kiválasztása a mentéshez:

`docker save --output {{path/to/file.tar}} {{image_name:tag1 image_name:tag2 ...}}`
