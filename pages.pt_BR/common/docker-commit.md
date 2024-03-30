# docker commit

> Criar uma nova imagem a partir das alterações em um contêiner.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/commit/>.

- Cria uma imagem a partir de um contêiner específico:

`docker commit {{contêiner}} {{imagem}}:{{tag}}`

- Aplica uma instrução `CMD` do Dockerfile à imagem criada:

`docker commit --change="CMD {{comando}}" {{contêiner}} {{imagem}}:{{tag}}`

- Aplica uma instrução `ENV` do Dockerfile à imagem criada:

`docker commit --change="ENV {{nome}}={{valor}}" {{contêiner}} {{imagem}}:{{tag}}`

- Cria uma imagem com um autor específico nos metadados:

`docker commit --author="{{autor}}" {{contêiner}} {{imagem}}:{{tag}}`

- Cria uma imagem com um comentário específico nos metadados:

`docker commit --message="{{comentário}}" {{contêiner}} {{imagem}}:{{tag}}`

- Cria uma imagem sem pausar o contêiner durante o commit:

`docker commit --pause={{false}} {{contêiner}} {{imagem}}:{{tag}}`

- Exibe ajuda:

`docker commit --help`
