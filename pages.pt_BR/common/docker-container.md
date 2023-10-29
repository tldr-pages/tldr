# docker container

> Gerenciar contêineres Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/container/>.

- Listar os contêineres Docker em execução:

`docker container ls`

- Iniciar um ou mais contêineres parados:

`docker container start {{nome_do_contêiner1}} {{nome_do_contêiner2}}`

- Encerrar um ou mais contêineres em execução:

`docker container kill {{nome_do_contêiner}}`

- Parar um ou mais contêineres em execução:

`docker container stop {{nome_do_contêiner}}`

- Pausar todos os processos em um ou mais contêineres:

`docker container pause {{nome_do_contêiner}}`

- Exibir informações detalhadas sobre um ou mais contêineres:

`docker container inspect {{nome_do_contêiner}}`

- Exportar o sistema de arquivos de um contêiner como um arquivo tar:

`docker container export {{nome_do_contêiner}}`

- Criar uma nova imagem a partir das alterações em um contêiner:

`docker container commit {{nome_do_contêiner}}`
