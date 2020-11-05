# docker secret

> Manage Docker swarm secret.
> More information: <https://docs.docker.com/engine/reference/commandline/secret/>.

- Create a new secret from stdin:

`printf {{secret_content}} | docker secret create {{secret_name}} -`

- Create a new secret from a file:

`docker secret create {{secret_name}} {{path/to/file}}`

- Display secrets list:

`docker secret ls`

- Display detailed information one one or multiple secrets in human friendly format:

`docker secret inspect --pretty {{secret_name1 secret_name2 ...}}`

- Remove one or more secrets:

`docker secret rm {{secret_name1 secret_name2 ...}}`
