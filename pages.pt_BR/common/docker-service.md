# docker service

> Gerenciar os serviços em um daemon do Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/service/>.

- Listar os serviços em um daemon do Docker:

`docker service ls`

- Criar um novo serviço:

`docker service create --name {{nome_do_serviço}} {{imagem}}:{{tag}}`

- Exibir informações detalhadas de uma lista separada por espaços de serviços:

`docker service inspect {{nome_do_serviço|ID}}`

- Listar as tarefas de uma lista separada por espaços de serviços:

`docker service ps {{nome_do_serviço|ID}}`

- Escalar para um número específico de réplicas para uma lista separada por espaços de serviços:

`docker service scale {{nome_do_serviço}}={{quantidade_de_réplicas}}`

- Remover uma lista separada por espaços de serviços:

`docker service rm {{nome_do_serviço|ID}}`
