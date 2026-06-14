# podman rmi

> Հեռացրեք OCI/Docker պատկերները:.
> Լրացուցիչ տեղեկություններ. <https://docs.podman.io/en/latest/markdown/podman-rmi.1.html>:.

- Հեռացրեք մեկ կամ մի քանի պատկեր՝ հաշվի առնելով նրանց անունները.:

`podman rmi {{image1:tag image2:tag ...}}`

- Ստիպել հեռացնել պատկերը.:

`podman rmi {{[-f|--force]}} {{image}}`

- Հեռացրեք պատկերը՝ առանց պիտակավորված ծնողներին ջնջելու.:

`podman rmi --no-prune {{image}}`

- Ցուցադրել օգնությունը.:

`podman rmi {{[-h|--help]}}`
