# skaffold

> Facilitate continuous development for Kubernetes applications.
> More information: <https://skaffold.dev/docs/references/cli/>.

- Build the artifacts:

`skaffold build {{[-f|--filename]}} {{skaffold.yaml}}`

- Build and deploy your app every time your code changes:

`skaffold dev {{[-f|--filename]}} {{skaffold.yaml}}`

- Run a pipeline file:

`skaffold run {{[-f|--filename]}} {{skaffold.yaml}}`

- Run a diagnostic on Skaffold:

`skaffold diagnose {{[-f|--filename]}} {{skaffold.yaml}}`

- Deploy the artifacts:

`skaffold deploy {{[-f|--filename]}} {{skaffold.yaml}}`
