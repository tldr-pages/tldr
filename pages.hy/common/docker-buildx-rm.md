# docker buildx rm

> Հեռացրեք մեկ կամ մի քանի շինարարական օրինակներ:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/buildx/rm/>:.

- Հեռացնել շինարարի օրինակը.:

`docker buildx rm {{builder_name}}`

- Հեռացրեք բոլոր ոչ ակտիվ շինարարները.:

`docker buildx rm --all-inactive`

- Հեռացրեք բոլոր անգործուն շինարարներին՝ առանց հաստատման պահանջելու.:

`docker buildx rm --all-inactive {{[-f|--force]}}`
