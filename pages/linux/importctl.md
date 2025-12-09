# importctl

> Download, Import, or Export disk images.
> More information: <https://www.freedesktop.org/software/systemd/man/importctl.html>.

- Download image in tarball format from a url via pull:

`sudo importctl pull-tar {{URL}} {{path/to/directory}}`

- Pull or download from a remote source that is either raw or qcow2 file, and stores it as a raw file:

`sudo importctl pull-raw {{https://example.com/source.ext}} {{name}} --class={{machine|portable|sysext|confext}}`

- Import a raw disk image into the image directory that is possibly compressed with xz, gzip, or bzip2:

`importctl import-raw {{path/to/file.ext}} {{name}} --class={{machine|portable|sysext|confext}}`

- Export a container image as tarball into current working directory:

`importctl export-tar --class={{machine|portable|sysext|confext}} {{name}} {{path/to/file.ext}}`
