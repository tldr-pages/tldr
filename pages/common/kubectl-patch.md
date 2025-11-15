# kubectl patch

> Patch Kubernetes resources with new values.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_patch>.

- Partially patch a secret using a strategic merge JSON patch to remove the finalizer:

`kubectl patch secrets {{secret_name}} {{[-p|--patch]}} '{"metadata":{"finalizers": []\}\}' --type merge`

- Partially patch a secret using a strategic merge YAML patch to remove the finalizer:

`kubectl patch secrets {{secret_name}} {{[-p|--patch]}} $'metadata:\n finalizers: []' --type merge`

- Partially patch a pod's container using a JSON patch with positional arrays:

`kubectl patch {{[po|pods]}} {{pod_name}} --type 'json' {{[-p|--patch]}} '[{"op": "replace", "path": "/spec/containers/0/image", "value":"{{new_image_value}}"}]'`

- Update a deployment's replicas through the scale subresource using a strategic merge JSON patch:

`kubectl patch {{[deploy|deployments]}} {{deployment_name}} --subresource 'scale' --type 'merge' {{[-p|--patch]}} '{"spec":{"replicas":{{number_of_replicas}}\}\}'`
