# docker images

> Zarządzaj obrazami Dockera.
> Więcej informacji: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Wyświetl wszystkie obrazy Docker:

`docker images`

- Wyświetl wszystkie obrazy Dockera, w tym intermediates:

`docker images {{[-a|--all]}}`

- Wyświetl dane wyjściowe w trybie quiet (tylko identyfikatory numeryczne):

`docker images {{[-q|--quiet]}}`

- Wyświetl wszystkie obrazy Docker nieużywane przez żaden kontener:

`docker images {{[-f|--filter]}} dangling=true`
