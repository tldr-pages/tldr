# helm

> Helm é um gerenciador de pacores para Kubernetes.
> Mais informações: <https://helm.sh/>.

- Cria um chart do helm:

`helm create {{nome_do_chart}}`

- Adiciona um novo repositório helm:

`helm repo add {{nome_do_repositório}}`

- Lista os repositórios helm:

`helm repo list`

- Atualiza os repositórios helm:

`helm repo update`

- Remova um repositório helm:

`helm repo remove {{nome_do_repositório}}`

- Instala um chart helm:

`helm install {{nome}} {{nome_do_repositório}}/{{nome_do_chart}}`

- Obtém um chart helm chart como um arquivo tar:

`helm get {{nome_do_release_do_chart}}`

- Atualiza as dependências helm:

`helm dependency update`
