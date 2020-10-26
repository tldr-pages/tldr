# helm

> Helm é um gerenciador de pacores para Kubernetes.
> Mais informações: <https://helm.sh/>.

- Cria um chart do helm:

`helm create {{chart_name}}`

- Adiciona um novo repositório helm:

`helm repo add {{repo_name}}`

- Lista os repositórios helm:

`helm repo list`

- Atualiza os repositórios helm:

`helm repo update`

- Remova um repositório helm:

`helm repo remove {{repo_name}}`

- Instala um chart helm:

`helm install {{repo_name}}/{{chart_name}}`

- Obtém um chart helm chart como um arquivo tar:

`helm get {{chart_release_name}}`

- Atualiza as dependências helm:

`helm dependency update`
