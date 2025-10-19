# docker-compose up

> Build, create, start, and attach to containers for a service.
> More information: <https://docs.docker.com/reference/cli/docker/compose/up/>.

- Create and start all containers in the background:

`docker-compose up --detach`

- Create and start all containers, rebuild images before starting:

`docker-compose up --build`

- Start all containers using an alternate compose file:

`docker-compose --file {{path/to/file.yml}} up`

- Create and start specific services:

`docker-compose up {{service1 service2}}`

- Create and start all containers, abort if any container fails to start:

`docker-compose up --abort-on-container-exit`

- Remove orphaned containers (containers that exist but are not defined in the compose file):

`docker-compose up --remove-orphans`

- Recreate containers even if their configuration hasn't changed:

`docker-compose up --force-recreate`

- Set a timeout for container startup (default is 10 seconds):

`docker-compose up --timeout {{30}}`
