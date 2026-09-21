# docker login

> Входить в реестр Docker.
> Больше информации: <https://docs.docker.com/reference/cli/docker/login/>.

- Войти в реестр в интерактивном режиме:

`docker login`

- Войти в реестр с определённым именем пользователя (будет запрошен пароль):

`docker login {{[-u|--username]}} {{имя_пользователя}}`

- Войти в реестр с именем пользователя и паролем:

`docker login {{[-u|--username]}} {{имя_пользователя}} {{[-p|--password]}} {{пароль}} {{сервер}}`

- Войти в реестр с паролем из `stdin`:

`echo "{{пароль}}" | docker login {{[-u|--username]}} {{имя_пользователя}} --password-stdin`
