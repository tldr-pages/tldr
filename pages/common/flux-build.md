# flux build

> Build Flux manifests.
> More information: <https://fluxcd.io/flux/cmd/flux_build/>.

- Build a Kustomization:

`flux build kustomization {{name}} --path={{path/to/kustomization}}`

- Build a Kustomization and output the manifests to a file:

`flux build kustomization {{name}} --path={{path/to/kustomization}} > {{path/to/manifests.yaml}}`

- Build a Kustomization and pipe it directly to `kubectl`:

`flux build kustomization {{name}} --path={{path/to/kustomization}} | kubectl apply -f -`
