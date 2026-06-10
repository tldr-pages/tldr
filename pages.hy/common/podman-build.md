# podman build

> Դեմոնային գործիք՝ կոնտեյների պատկերներ կառուցելու համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.podman.io/en/latest/markdown/podman-build.1.html>:.

- Ստեղծեք պատկեր՝ օգտագործելով `Dockerfile` կամ `Containerfile` նշված գրացուցակում.:

`podman build {{path/to/directory}}`

- Ստեղծեք պատկեր նշված պիտակով.:

`podman build {{[-t|--tag]}} {{image_name:version}} {{path/to/directory}}`

- Ստեղծեք պատկեր ոչ ստանդարտ ֆայլից.:

`podman build {{[-f|--file]}} {{Containerfile.different}} .`

- Ստեղծեք պատկեր առանց նախկինում պահված պատկերների օգտագործման.:

`podman build --no-cache {{path/to/directory}}`

- Ստեղծեք պատկեր, որը ճնշում է բոլոր ելքերը.:

`podman build {{[-q|--quiet]}} {{path/to/directory}}`
