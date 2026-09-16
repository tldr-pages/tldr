# docker image pull

> Unduh citra-citra Docker dari suatu registri.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/image/pull/>.

- Unduh suatu citra Docker secara spesifik:

`docker {{[pull|image pull]}} {{citra}}:{{tag}}`

- Unduh citra Docker dalam mode sunyi:

`docker {{[pull|image pull]}} {{[-q|--quiet]}} {{citra}}:{{tag}}`

- Unduh seluruh tag untuk suatu citra Docker:

`docker {{[pull|image pull]}} {{[-a|--all-tags]}} {{citra}}`

- Unduh suatu citra Docker untuk platform tertentu:

`docker {{[pull|image pull]}} --platform {{linux/amd64}} {{citra}}:{{tag}}`

- Tampilkan bantuan:

`docker {{[pull|image pull]}} --help`
