# docker build

> Build an image from a Dockerfile.
> More information: <https://docs.docker.com/engine/reference/commandline/build/>.

- Build a docker image using the Dockerfile in the current directory:

`docker build .`

- Build a docker image from a Dockerfile at a specified URL:

`docker build {{github.com/creack/docker-firefox}}`

- Build a docker image and tag it:

`docker build --tag {{name:tag}} .`

- Do not use the cache when building the image:

`docker build --no-cache --tag {{name:tag}} .`

- Build a docker image using a specific Dockerfile:

`docker build --file {{Dockerfile}} .`

- Build with custom build-time variables:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
