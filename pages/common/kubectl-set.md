# kubectl set

> Update fields of Kubernetes resources.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_set/>.

- Set a deployment's nginx container image to nginx:1.9.1:

`kubectl set image {{[deploy|deployment]}}/{{deployment_name}} {{container_name}}={{nginx:1.9.1}}`

- Update all deployments and replication controllers in the current namespace to use the nginx:1.9.1 image:

`kubectl set image {{[deploy|deployments]}} {{[rc|replicationcontrollers]}} *={{nginx:1.9.1}}`

- Update the resources (CPU/memory) of a deployment:

`kubectl set resources {{[deploy|deployment]}}/{{deployment_name}} --limits {{cpu}}={{200m}},{{memory}}={{512Mi}}`

- Set the environment variable for a deployment:

`kubectl set env {{[deploy|deployment]}}/{{deployment_name}} {{KEY}}={{value}}`

- Remove an environment variable from a deployment:

`kubectl set env {{[deploy|deployment]}}/{{deployment_name}} {{KEY}}-`

- Display help:

`kubectl set --help`
