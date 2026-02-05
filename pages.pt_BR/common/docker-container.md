# docker container

> Gerenciar contêineres Docker.
> Mais informações: <https://docs.docker.com/reference/cli/docker/container/>.

- Lista os contêineres Docker em execução:

`docker {{[ps|container ls]}}`

- Inicia um ou mais contêineres parados:

`docker {{[start|container start]}} {{nome_do_contêiner1}} {{nome_do_contêiner2}}`

- Encerra um ou mais contêineres em execução:

`docker {{[kill|container kill]}} {{nome_do_contêiner}}`

- Para um ou mais contêineres em execução:

`docker {{[stop|container stop]}} {{nome_do_contêiner}}`

- Pausa todos os processos em um ou mais contêineres:

`docker {{[pause|container pause]}} {{nome_do_contêiner}}`

- Exibe informações detalhadas sobre um ou mais contêineres:

`docker container inspect {{nome_do_contêiner}}`

- Exporta o sistema de arquivos de um contêiner como um arquivo `.tar`:

`docker {{[export|container export]}} {{nome_do_contêiner}}`

- Cria uma nova imagem a partir das alterações em um contêiner:

`docker {{[commit|container commit]}} {{nome_do_contêiner}}`
