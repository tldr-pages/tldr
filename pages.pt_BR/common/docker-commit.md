# docker commit

> Criar uma nova imagem a partir das alterações em um contêiner.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/commit/>.

- Criar uma imagem a partir de um contêiner específico:

`docker commit {{contêiner}} {{imagem}}:{{tag}}`

- Aplicar uma instrução `CMD` do Dockerfile à imagem criada:

`docker commit --change="CMD {{comando}}" {{contêiner}} {{imagem}}:{{tag}}`

- Aplicar uma instrução `ENV` do Dockerfile à imagem criada:

`docker commit --change="ENV {{nome}}={{valor}}" {{contêiner}} {{imagem}}:{{tag}}`

- Criar uma imagem com um autor específico nos metadados:

`docker commit --author="{{autor}}" {{contêiner}} {{imagem}}:{{tag}}`

- Criar uma imagem com um comentário específico nos metadados:

`docker commit --message="{{comentário}}" {{contêiner}} {{imagem}}:{{tag}}`

- Criar uma imagem sem pausar o contêiner durante o commit:

`docker commit --pause={{false}} {{contêiner}} {{imagem}}:{{tag}}`

- Exibir ajuda:

`docker commit --help`
