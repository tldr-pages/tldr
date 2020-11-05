# docker save

> Export one or more docker images to archive.
> More information: <https://docs.docker.com/engine/reference/commandline/save/>.

- Save the image by redirecting output to a file:

`docker save {{image}} > {{path/to/file}}`

- Save an image to a tar archive:

`docker save --output {{/path/to/file.tar}} {{image}}`

- Save all tags of the image:

`docker save --output {{/path/to/file.tar}} {{image_name}}`

- Use gzip to save the image:

`docker save {{image}} | gzip > {{/path/to/file.tar.gz}}`

- Cherry-pick particular tags of an image to save:

`docker save --output {{/path/to/file.tar}} {{image_name:tag1 image_name:tag2 ...}}`
