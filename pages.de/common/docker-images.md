# docker images

> Verwalte Docker Images.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/images/>.

- Liste alle Docker Images auf:

`docker images`

- Liste alle Docker Images inkl. Zwischen-Images auf:

`docker images --all`

- Liste nur die IDs der Docker Images auf:

`docker images --quiet`

- Liste alle Docker Images auf, die nicht von einem Container verwendet werden:

`docker images --filter dangling=true`

- Liste alle Docker Images mit einer bestimmten Zeichenfolge im Namen auf:

`docker images "{{*name*}}"`
