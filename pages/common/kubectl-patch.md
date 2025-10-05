# kubectl patch

> Patches Kubernetes resources with new values.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#patch>.

- Partially patch a secret using a strategic merge JSON patch to remove the finalizer:

`kubectl patch secret {{secret_name}} -p '{"metadata":{"finalizers": []}}' --type merge`

- Partially patch a secret using a strategic merge YAML patch to remove the finalizer:

`kubectl patch secret {{secret_name}} -p $'metadata:\n finalizers: []' --type merge`

- Partially patch a pod's container using a JSON patch with positional arrays:

`kubectl patch {{[po|pod]}} {{pod_name}} --type='json' -p='[{"op": "replace", "path": "/spec/containers/0/image", "value":"{{new_image_value}}"}]'`

- Update a deployment's replicas through the scale subresource using a strategic merge JSON patch:

`kubectl patch {{[deploy|deployment]}} {{deployment_name}} --subresource='scale' --type='merge' -p '{"spec":{"replicas":{{number_of_replicas}}}}'`
