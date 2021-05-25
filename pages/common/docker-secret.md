# docker secret

> Manage Docker swarm secrets.
> More information: <https://docs.docker.com/engine/reference/commandline/secret/>.

- Create a new secret from stdin:

`{{command}} | docker secret create {{secret_name}} -`

- Create a new secret from a file:

`docker secret create {{secret_name}} {{path/to/file}}`

- List all secrets:

`docker secret ls`

- Display detailed information on one or multiple secrets in a human friendly format:

`docker secret inspect --pretty {{secret_name1 secret_name2 ...}}`

- Remove one or more secrets:

`docker secret rm {{secret_name1 secret_name2 ...}}`
