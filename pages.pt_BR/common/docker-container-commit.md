# docker container commit

> Criar uma nova imagem a partir das alterações em um contêiner.
> Mais informações: <https://docs.docker.com/reference/cli/docker/container/commit/>.

- Cria uma imagem a partir de um contêiner específico:

`docker {{[commit|container commit]}} {{contêiner}} {{imagem}}:{{tag}}`

- Aplica uma instrução `CMD` do Dockerfile à imagem criada:

`docker {{[commit|container commit]}} {{[-c|--change]}} "CMD {{comando}}" {{contêiner}} {{imagem}}:{{tag}}`

- Aplica uma instrução `ENV` do Dockerfile à imagem criada:

`docker {{[commit|container commit]}} {{[-c|--change]}} "ENV {{nome}}={{valor}}" {{contêiner}} {{imagem}}:{{tag}}`

- Cria uma imagem com um autor específico nos metadados:

`docker {{[commit|container commit]}} {{[-a|--author]}} "{{autor}}" {{contêiner}} {{imagem}}:{{tag}}`

- Cria uma imagem com um comentário específico nos metadados:

`docker {{[commit|container commit]}} {{[-m|--message]}} "{{comentário}}" {{contêiner}} {{imagem}}:{{tag}}`

- Cria uma imagem sem pausar o contêiner durante o commit:

`docker {{[commit|container commit]}} {{[-p|--pause]}} false {{contêiner}} {{imagem}}:{{tag}}`

- Exibe ajuda:

`docker {{[commit|container commit]}} --help`
