# docker image ls

> Zarządzaj obrazami Dockera.
> Więcej informacji: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Wyświetl wszystkie obrazy Docker:

`docker {{[images|image ls]}}`

- Wyświetl wszystkie obrazy Dockera, w tym intermediates:

`docker {{[images|image ls]}} {{[-a|--all]}}`

- Wyświetl dane wyjściowe w trybie quiet (tylko identyfikatory numeryczne):

`docker {{[images|image ls]}} {{[-q|--quiet]}}`

- Wyświetl wszystkie obrazy Docker nieużywane przez żaden kontener:

`docker {{[images|image ls]}} {{[-f|--filter]}} dangling=true`
