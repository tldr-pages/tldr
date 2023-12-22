# docker network

> Criar e gerenciar redes do Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/network/>.

- Lista todas as redes disponíveis e configuradas no daemon do Docker:

`docker network ls`

- Cria uma rede definida pelo usuário:

`docker network create --driver {{nome_do_driver}} {{nome_da_rede}}`

- Exibe informações detalhadas de uma lista separada por espaços de redes:

`docker network inspect {{nome_da_rede}}`

- Conecta um contêiner a uma rede usando um nome ou ID:

`docker network connect {{nome_da_rede}} {{nome_do_contêiner|ID}}`

- Desconecta um contêiner de uma rede:

`docker network disconnect {{nome_da_rede}} {{nome_do_contêiner|ID}}`

- Remove todas as redes não utilizadas (que não são referenciadas por nenhum contêiner):

`docker network prune`

- Remove uma lista separada por espaços de redes não utilizadas:

`docker network rm {{nome_da_rede}}`
