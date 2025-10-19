# docker-compose up

> Start and run Docker services defined in a Compose file.
> More information: <https://docs.docker.com/compose/reference/up/>.

- Start all services defined in the docker-compose file:

`docker-compose up`

- Start services in the background (detached mode):

`docker-compose up {{[-d|--detach]}}`

- Start services and rebuild images before starting:

`docker-compose up --build`

- Start specific services only:

`docker-compose up {{service1 service2 ...}}`

- Start services with custom compose file:

`docker-compose {{[-f|--file]}} {{path/to/docker-compose.yml}} up`

- Start services and remove orphaned containers:

`docker-compose up --remove-orphans`

- Start services with scaled instances:

`docker-compose up --scale {{service}}={{count}}`

- Start services and show logs with timestamps:

`docker-compose up --timestamps`
