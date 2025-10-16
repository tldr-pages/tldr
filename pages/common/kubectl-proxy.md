# kubectl proxy

> Create a proxy server between localhost and the Kubernetes API server.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_proxy/>.

- Start a proxy server on the default port (8001):

`kubectl proxy`

- Start a proxy server on a specific port:

`kubectl proxy --port {{9000}}`

- Accept connections from all interfaces (not just localhost):

`kubectl proxy --address {{0.0.0.0}} --accept-hosts '{{.*}}'`

- Start proxy and reject paths matching a regex:

`kubectl proxy --reject-paths {{'^/api/.*/pods/.*'}}`

- Start proxy with a specific API prefix:

`kubectl proxy --api-prefix {{/custom/}}`
