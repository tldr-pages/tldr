# skaffold

> Facilitate continuous development for Kubernetes applications.
> More information: <https://skaffold.dev>.

- Build the artifacts:

`skaffold build -f {{skaffold.yaml}}`

- Build and deploy your app every time your code changes:

`skaffold dev -f {{skaffold.yaml}}`

- Run a pipeline file:

`skaffold run -f {{skaffold.yaml}}`

- Run a diagnostic on Skaffold:

`skaffold diagnose -f {{skaffold.yaml}}`

- Deploy the artifacts:

`skaffold deploy -f {{skaffold.yaml}}`
