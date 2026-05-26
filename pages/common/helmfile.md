# helmfile

> Declare and manage Helm releases and related Kubernetes manifests.
> More information: <https://helmfile.readthedocs.io>.

- Install required Helm plugins:

`helmfile init`

- Preview the changes that would be applied to the cluster:

`helmfile diff`

- Apply releases defined in `helmfile.yaml` to the cluster:

`helmfile apply`

- Synchronize the cluster with the desired state, force-recreating if needed:

`helmfile sync`

- Apply releases for a specific environment:

`helmfile {{[-e|--environment]}} {{dev|production|staging}} apply`

- Destroy all releases defined in `helmfile.yaml`:

`helmfile destroy`

- Display help:

`helmfile {{[-h|--help]}}`

- Display version:

`helmfile version`
