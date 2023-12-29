# docker swarm

> Uma ferramenta de orquestração de contêineres.
> Mais informações: <https://docs.docker.com/engine/swarm/>.

- Inicializa um cluster do Swarm:

`docker swarm init`

- Exibe o token para ingressar como gerenciador ou trabalhador:

`docker swarm join-token {{worker|manager}}`

- Ingressa um novo nó ao cluster:

`docker swarm join --token {{token}} {{url_do_nó_gerenciador:2377}}`

- Remove um trabalhador do Swarm (executado dentro do nó trabalhador):

`docker swarm leave`

- Exibe o certificado CA atual no formato PEM:

`docker swarm ca`

- Rotaciona o certificado CA atual e exibe o novo certificado:

`docker swarm ca --rotate`

- Altera o período de validade dos certificados dos nós:

`docker swarm update --cert-expiry {{horas}}h{{minutos}}m{{segundos}}s`
