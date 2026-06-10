# kubectl-ի թողարկում

> Կառավարեք Kubernetes-ի ռեսուրսի տարածումը (տեղակայումներ, դեմոնսեթներ և վիճակագրություններ):.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/>:.

- Սկսեք ռեսուրսի շարժական վերագործարկում.:

`kubectl rollout restart {{resource_type}}/{{resource_name}}`

- Դիտեք ռեսուրսի շարժական թարմացման կարգավիճակը.:

`kubectl rollout status {{resource_type}}/{{resource_name}}`

- Վերադարձեք ռեսուրսը նախորդ վերանայմանը.:

`kubectl rollout undo {{resource_type}}/{{resource_name}}`

- Դիտեք ռեսուրսի թողարկման պատմությունը.:

`kubectl rollout history {{resource_type}}/{{resource_name}}`
