# ko

> Build and deploy Go applications as container images on Kubernetes.
> More information: <https://ko.build/reference/ko/>.

- Build and publish a container image from a Go package import path:

`ko build {{import_path}}`

- Apply Kubernetes manifests with Go image references resolved to digests:

`ko apply {{[-f|--filename]}} {{path/to/manifest.yaml}}`

- Create Kubernetes resources with resolved image references:

`ko create {{[-f|--filename]}} {{path/to/manifest.yaml}}`

- Print resolved Kubernetes manifests without applying them:

`ko resolve {{[-f|--filename]}} {{path/to/manifest.yaml}}`

- Build and run a Go package on Kubernetes:

`ko run {{import_path}}`

- Delete Kubernetes resources defined in a manifest:

`ko delete {{[-f|--filename]}} {{path/to/manifest.yaml}}`

- Log in to a container registry:

`ko login {{registry.example.com}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}}`
