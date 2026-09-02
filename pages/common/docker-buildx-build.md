# docker buildx build

> Build an image from a Dockerfile using the BuildKit engine.
> More information: <https://docs.docker.com/reference/cli/docker/buildx/build>.

- Build an image from the Dockerfile in the current directory:

`docker buildx build .`

- Build an image and tag it:

`docker buildx build -t {{image:tag}} .`

- Build an image using a specific Dockerfile:

`docker buildx build {{[-f|--file]}} {{path/to/Dockerfile}} .`

- Build an image passing build-time variables:

`docker buildx build --build-arg {{HTTP_PROXY=http://proxy.example.com}} --build-arg {{VERSION=1.0}} .`

- Build an image without using the build cache:

`docker buildx build --no-cache .`

- Build an image and load it into `docker images`:

`docker buildx build --load -t {{image:tag}} .`

- Build for multiple platforms and push to a registry:

`docker buildx build --platform {{linux/amd64,linux/arm64}} --push -t {{registry.example.com/image:tag}} .`

- Build a specific stage from a multi-stage Dockerfile:

`docker buildx build --target {{stage_name}} -t {{image:tag}} .`
