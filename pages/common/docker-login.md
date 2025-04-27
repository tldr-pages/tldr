# docker login

> Log into a Docker registry.
> More information: <https://docs.docker.com/reference/cli/docker/login/>.

- Interactively log into a registry:

`docker login`

- Log into a registry with a specific username (user will be prompted for a password):

`docker login {{[-u|--username]}} {{username}}`

- Log into a registry with username and password:

`docker login {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} {{server}}`

- Log into a registry with password from `stdin`:

`echo "{{password}}" | docker login {{[-u|--username]}} {{username}} --password-stdin`
