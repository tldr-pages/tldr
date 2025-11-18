# kubectl delete

> Exclui um recurso usando nome de arquivo, entrada padrão (stdin), recurso e nome, ou recurso e seletor de rótulo.
> Mais informações: <https://kubernetes.io/docs/reference/kubectl/cheatsheet/>.

- Excluir um pod pelo nome:

`kubectl delete pod {{pod_name}}`

- Excluir um deployment identificado em 'deployment.yaml':

`kubectl delete -f {{path/to/deployment.yaml}}`

- Excluir todos os pods e services com um rótulo específico:

`kubectl delete pod,service -l {{label_name}}={{label_value}}`

- Excluir todos os recursos em um determinado namespace:

`kubectl delete all --all -n {{namespace}}`

- Excluir todos os deployments e services em um namespace especificado:

`kubectl delete {{[deploy|deployments]}},{{[svc|services]}} --all {{[-n|--namespace]}} {{namespace}}`

- Excluir todos os nodes:

`kubectl delete {{[no|nodes]}} --all`

- Excluir recursos definidos em um manifesto YAML:

`kubectl delete {{[-f|--filename]}} {{path/to/manifest.yaml}}`
