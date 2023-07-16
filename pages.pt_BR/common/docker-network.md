# docker network

> Criar e gerenciar redes do Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/network/>.

- Listar todas as redes disponíveis e configuradas no daemon do Docker:

`docker network ls`

- Criar uma rede definida pelo usuário:

`docker network create --driver {{nome_do_driver}} {{nome_da_rede}}`

- Exibir informações detalhadas de uma lista separada por espaços de redes:

`docker network inspect {{nome_da_rede}}`

- Conectar um contêiner a uma rede usando um nome ou ID:

`docker network connect {{nome_da_rede}} {{nome_do_contêiner|ID}}`

- Desconectar um contêiner de uma rede:

`docker network disconnect {{nome_da_rede}} {{nome_do_contêiner|ID}}`

- Remover todas as redes não utilizadas (que não são referenciadas por nenhum contêiner):

`docker network prune`

- Remover uma lista separada por espaços de redes não utilizadas:

`docker network rm {{nome_da_rede}}`
