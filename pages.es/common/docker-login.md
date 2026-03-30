# docker login

> Inicia sesión en un registro de Docker.
> Más información: <https://docs.docker.com/reference/cli/docker/login/>.

- Inicia sesión en un registro de forma interactiva:

`docker login`

- Inicia sesión en un registro con un nombre de usuario específico (se pedirá la contraseña):

`docker login {{[-u|--username]}} {{usuario}}`

- Inicia sesión en un registro con usuario y contraseña:

`docker login {{[-u|--username]}} {{usuario}} {{[-p|--password]}} {{contraseña}} {{servidor}}`

- Inicia sesión en un registro con la contraseña desde `stdin`:

`echo "{{contraseña}}" | docker login {{[-u|--username]}} {{usuario}} --password-stdin`
