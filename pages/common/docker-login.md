# docker login

> Log into a docker registry.
> More information: <https://docs.docker.com/engine/reference/commandline/login/>.

- Log into registry with username and password:

`docker login -u {{username}} -p {{password}} {{server}}`

- Log into registry with password from stdin:

`{{cat path/to/password.txt}} | docker login -u {{username}} --password-stdin`
