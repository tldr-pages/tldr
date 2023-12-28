# docker service

> Gerenciar os serviços em um daemon do Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/service/>.

- Lista os serviços em um daemon do Docker:

`docker service ls`

- Cria um novo serviço:

`docker service create --name {{nome_do_serviço}} {{imagem}}:{{tag}}`

- Exibe informações detalhadas de uma lista separada por espaços de serviços:

`docker service inspect {{nome_do_serviço|ID}}`

- Lista as tarefas de uma lista separada por espaços de serviços:

`docker service ps {{nome_do_serviço|ID}}`

- Escala para um número específico de réplicas para uma lista separada por espaços de serviços:

`docker service scale {{nome_do_serviço}}={{quantidade_de_réplicas}}`

- Remove uma lista separada por espaços de serviços:

`docker service rm {{nome_do_serviço|ID}}`
