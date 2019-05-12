# popeye

> Utility that reports potential issues with your Kubernetes deployment manifests and configuration.
> Homepage: <https://github.com/derailed/popeye>.

- Scan your Kubernetes cluster:

`popeye`

- Scan specific namespace:

`popeye -n {{namespace}}`

- Scan specific Kubernetes context:

`popeye --context={{context}}`

- Use spinach config file for scanning:

`popeye -f {{spinach.yaml}}`
