# docker container

> Gerenciar contêineres Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/container/>.

- Lista os contêineres Docker em execução:

`docker container ls`

- Inicia um ou mais contêineres parados:

`docker container start {{nome_do_contêiner1}} {{nome_do_contêiner2}}`

- Encerra um ou mais contêineres em execução:

`docker container kill {{nome_do_contêiner}}`

- Para um ou mais contêineres em execução:

`docker container stop {{nome_do_contêiner}}`

- Pausa todos os processos em um ou mais contêineres:

`docker container pause {{nome_do_contêiner}}`

- Exibe informações detalhadas sobre um ou mais contêineres:

`docker container inspect {{nome_do_contêiner}}`

- Exporta o sistema de arquivos de um contêiner como um arquivo tar:

`docker container export {{nome_do_contêiner}}`

- Cria uma nova imagem a partir das alterações em um contêiner:

`docker container commit {{nome_do_contêiner}}`
