# kubectl set

> Update fields of existing application resources.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/>.

- Update the image of a container in a deployment:

`kubectl set image {{[deploy|deployment]}}/{{deployment_name}} {{container_name}}={{image}}`

- Update the image of all containers in a deployment:

`kubectl set image {{[deploy|deployment]}}/{{deployment_name}} *={{image}}`

- Set resource limits (CPU and memory) on a deployment:

`kubectl set resources {{[deploy|deployment]}}/{{deployment_name}} --limits cpu={{cpu_limit}},memory={{memory_limit}}`

- Set an environment variable on a deployment:

`kubectl set env {{[deploy|deployment]}}/{{deployment_name}} {{variable_name}}={{value}}`

- Remove an environment variable from a deployment:

`kubectl set env {{[deploy|deployment]}}/{{deployment_name}} {{variable_name}}-`

- Import environment variables from a secret or ConfigMap:

`kubectl set env --from {{[secret|configmap]}}/{{resource_name}} {{[deploy|deployment]}}/{{deployment_name}}`

- Update the service account of a deployment:

`kubectl set {{[sa|serviceaccount]}} {{[deploy|deployment]}}/{{deployment_name}} {{service_account_name}}`
