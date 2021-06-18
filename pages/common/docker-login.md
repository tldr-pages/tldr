# docker login

> Log into a docker registry.
> More information: <https://docs.docker.com/engine/reference/commandline/login/>.

- Log into registry with username and password:

`docker login --username {{username}} --password {{password}} {{server}}`

- Log into registry with password from stdin:

` echo "{{password}}" | docker login --username {{username}} --password-stdin`
