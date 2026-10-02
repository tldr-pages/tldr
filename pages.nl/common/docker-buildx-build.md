# docker buildx build

> Bouw een image vanuit een Dockerfile met de BuildKit-engine.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/buildx/build>.

- Bouw een image vanuit de Dockerfile in de huidige map:

`docker buildx build .`

- Bouw een image en voorzie deze van een tag:

`docker buildx build {{[-t|--tag]}} {{image:tag}} .`

- Bouw een image met een specifieke Dockerfile:

`docker buildx build {{[-f|--file]}} {{pad/naar/Dockerfile}} .`

- Bouw een image met build-time variabelen:

`docker buildx build --build-arg {{HTTP_PROXY=http://proxy.example.com}} --build-arg {{VERSION=1.0}} .`

- Bouw een image zonder de build-cache te gebruiken:

`docker buildx build --no-cache .`

- Bouw een image en laad deze in `docker images`:

`docker buildx build --load {{[-t|--tag]}} {{image:tag}} .`

- Bouw voor meerdere platformen en push naar een registry:

`docker buildx build --platform {{linux/amd64,linux/arm64}} --push {{[-t|--tag]}} {{registry.example.com/image:tag}} .`

- Bouw een specifieke stage vanuit een multi-stage Dockerfile:

`docker buildx build --target {{stage_naam}} {{[-t|--tag]}} {{image:tag}} .`
