# docker-compose

> Run and manage multi container docker applications

- Create and start containers in the background using a local `docker-compose.yml` file:

`docker-compose up -d`

- Start containers, rebuild if necessary:

`docker-compose up --build`

- Start containers using a custom configuration file:

`docker-compose --file {{path/to/config}} up`

- Stop running containers:

`docker-compose stop`

- Stop and remove containers, networks, images, and volumes:

`docker-compose down`

- Follow logs:

`docker-compose logs --follow`
