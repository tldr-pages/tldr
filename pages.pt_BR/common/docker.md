# docker

> Gerenciador de containers e imagens Docker.
> Alguns subcomandos como `docker run` tem sua própia documentação de uso.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/cli/>.

- Lista os containers Docker que se encontram em execução:

`docker ps`

- Lista todos os containers Docker:

`docker ps -a`

- Inicializa um container com um nome personalizado a partir de uma imagem:

`docker run --name {{nome_container}} {{imagem}}`

- Começa ou para um container existente:

`docker {{start|stop}} {{nome_container}}`

- Extrai uma imagem a partir de um Docker Registry:

`docker pull {{imagem}}`

- Abre um terminal dentro de um container em execução:

`docker exec -it {{nome_container}} {{sh}}`

- Remove um container parado:

`docker rm {{nome_container}}`

- Obtém e acompanha o histórico de um container:

`docker logs -f {{nome_container}}`
