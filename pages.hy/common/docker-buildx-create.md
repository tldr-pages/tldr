# docker buildx ստեղծել

> Ստեղծեք շինարարի նոր օրինակ:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/buildx/create/>:.

- Ստեղծեք շինարարի նոր օրինակ՝ օգտագործելով լռելյայն Docker համատեքստը.:

`docker buildx create`

- Ստեղծեք նոր շինարարական օրինակ հատուկ անունով.:

`docker buildx create --name {{builder_name}}`

- Ստեղծեք շինարարի նոր օրինակ և անմիջապես դրեք այն որպես ընթացիկ ակտիվ շինարար.:

`docker buildx create --name {{builder_name}} --use`

- Ստեղծեք շինարարի նոր օրինակ՝ օգտագործելով հատուկ դրայվեր (կանխադրված է `docker`):

`docker buildx create --driver {{docker-container|kubernetes|remote|...}}`

- Ստեղծեք շինարարի նոր օրինակ հատուկ աջակցվող հարթակներով.:

`docker buildx create --platform {{linux/amd64,linux/arm64,...}}`

- Կցեք նոր հանգույց գոյություն ունեցող շինարարին.:

`docker buildx create --name {{builder_name}} --append {{context|endpoint}}`

- Ստեղծեք շինարարի նոր օրինակ հատուկ BuildKit daemon դրոշներով.:

`docker buildx create --buildkitd-flags "{{--debug --debugaddr 0.0.0.0:6666}}"`

- Ստեղծեք շինարարի նոր օրինակ և անմիջապես բեռնեք այն.:

`docker buildx create --name {{builder_name}} --bootstrap`
