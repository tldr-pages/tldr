# kubectl

> Linha de comando para executar comando em clusters do Kubernetes.
> Alguns subcomandos como `kubectl run` tem sua própia documentação de uso.
> Mais informações: <https://kubernetes.io/docs/reference/kubectl/>.

- Lista toda a informação sobre um recurso em detalhes:

`kubectl get {{pod|service|deployment|ingress|...}} -o wide`

- Atualiza um pod específico com o label 'unhealthy' e o valor 'true':

`kubectl label pods {{name}} unhealthy=true`

- Lista todos os recursos de diferentes tipos:

`kubectl get all`

- Exibe os usos de recursos (CPU/Memória/Espaço alocado) dos nós ou pods:

`kubectl top {{pod|node}}`

- Exibe os endereços dos serviços do master e do cluster:

`kubectl cluster-info`

- Exibe uma explicação de um campo específico:

`kubectl explain {{pods.spec.containers}}`

- Exibe os logs de um container em um pod ou de um recurso específico:

`kubectl logs {{pod_name}}`

- Executa um comando em um pod existente:

`kubectl exec {{pod_name}} -- {{ls /}}`
