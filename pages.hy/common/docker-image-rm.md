# docker պատկեր rm

> Հեռացրեք Docker պատկերները:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/image/rm/>:.

- Հեռացրեք մեկ կամ մի քանի պատկեր՝ հաշվի առնելով նրանց անունները.:

`docker {{[rmi|image rm]}} {{image1 image2 ...}}`

- Ստիպել հեռացնել պատկերը.:

`docker {{[rmi|image rm]}} {{[-f|--force]}} {{image}}`

- Հեռացրեք պատկերը՝ առանց պիտակավորված ծնողներին ջնջելու.:

`docker {{[rmi|image rm]}} --no-prune {{image}}`

- Ցուցադրել օգնությունը.:

`docker {{[rmi|image rm]}} --help`
