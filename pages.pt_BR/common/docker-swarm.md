# docker swarm

> Uma ferramenta de orquestração de contêineres.
> Mais informações: <https://docs.docker.com/engine/swarm/>.

- Inicializar um cluster do Swarm:

`docker swarm init`

- Exibir o token para ingressar como gerenciador ou trabalhador:

`docker swarm join-token {{worker|manager}}`

- Ingressar um novo nó ao cluster:

`docker swarm join --token {{token}} {{url_do_nó_gerenciador:2377}}`

- Remover um trabalhador do Swarm (executado dentro do nó trabalhador):

`docker swarm leave`

- Exibir o certificado CA atual no formato PEM:

`docker swarm ca`

- Rotacionar o certificado CA atual e exibir o novo certificado:

`docker swarm ca --rotate`

- Alterar o período de validade dos certificados dos nós:

`docker swarm update --cert-expiry {{horas}}h{{minutos}}m{{segundos}}s`
