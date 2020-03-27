# docker build

> Build an image from a Dockerfile.
> More information: <https://docs.docker.com/engine/reference/commandline/build/>.

- Build an docker image using the Dockerfile in current directory:

`docker build .`

- Build an docker image with URL:

`docker build {{github.com/creack/docker-firefox}}`

- Build an docker image and tag it:

`docker build --tag {{name:tag}} .`

- Do not use cache when building the image:

`docker build --no-cache --tag {{name:tag}} .`

- Build an docker image using a specific Dockerfile:

`docker build -f {{Dockerfile}} .`

- Build with custom build-time variables:

`docker build --build-arg {{HTTP_PROXY=http://10.20.30.2:1234}} --build-arg {{FTP_PROXY=http://40.50.60.5:4567}} .`
