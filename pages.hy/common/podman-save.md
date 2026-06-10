# podman խնայողություն

> Պահպանեք պատկերը տեղական ֆայլում կամ գրացուցակում:.
> Տես նաև՝ `podman load`, `podman export`:.
> Լրացուցիչ տեղեկություններ. <https://docs.podman.io/en/latest/markdown/podman-save.1.html>:.

- Պահպանեք պատկերը `.tar` ֆայլում՝:

`podman save {{[-o|--output]}} {{path/to/file.tar}} {{image:tag}}`

- Պահպանեք պատկերը `stdout`-ում:

`podman save {{image:tag}} > {{path/to/file.tar}}`

- Պահպանեք պատկերը սեղմումով.:

`podman save {{image:tag}} | {{[gzip|bzip2|xz|zstd|zstdchunked]}} > {{path/to/file.tar[.gz|.bz2|.xz|.zst|.zst]}}`

- Պատկերը փոխանցեք հեռավոր համակարգին, սեղմելով և առաջընթացի բարով.:

`podman save {{image:tag}} | zstd {{[-T|--threads]}} 0 --ultra | pv | ssh {{username}}@{{remote_host}} podman load`
