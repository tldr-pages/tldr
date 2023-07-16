# docker login

> Fazer login em um registro do Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/login/>.

- Fazer login interativamente em um registro:

`docker login`

- Fazer login em um registro com um nome de usuário específico (será solicitada a senha):

`docker login --username {{nome_de_usuário}}`

- Fazer login em um registro com nome de usuário e senha:

`docker login --username {{nome_de_usuário}} --password {{senha}} {{servidor}}`

- Fazer login em um registro com a senha vinda do `stdin`:

`echo "{{senha}}" | docker login --username {{nome_de_usuário}} --password-stdin`
