# popeye

> Utility that reports potential issues with Kubernetes deployment manifests.
> More information: <https://github.com/derailed/popeye>.

- Scan the current Kubernetes cluster:

`popeye`

- Scan a specific namespace:

`popeye -n {{namespace}}`

- Scan specific Kubernetes context:

`popeye --context={{context}}`

- Use a spinach configuration file for scanning:

`popeye -f {{spinach.yaml}}`
