# helm template

> Render the templates of a helm chart locally, without installing it.
> More information: <https://helm.sh/docs/helm/helm_template/>.

- Render a chart from a repository:

`helm template {{release_name}} {{repository_name}}/{{chart_name}}`

- Render a chart from an unpacked chart directory:

`helm template {{release_name}} {{path/to/source_directory}}`

- Render a chart with a custom values file:

`helm template {{release_name}} {{repository_name}}/{{chart_name}} {{[-f|--values]}} {{path/to/values.yaml}}`

- Render a chart with custom values:

`helm template {{release_name}} {{repository_name}}/{{chart_name}} --set {{parameter1}}={{value1}},{{parameter2}}={{value2}}`

- Render only a specific template of a chart:

`helm template {{release_name}} {{repository_name}}/{{chart_name}} {{[-s|--show-only]}} {{templates/deployment.yaml}}`

- Write the rendered templates to files in a directory:

`helm template {{release_name}} {{repository_name}}/{{chart_name}} --output-dir {{path/to/output_directory}}`

- Render a chart including its custom resource definitions:

`helm template {{release_name}} {{repository_name}}/{{chart_name}} --include-crds`

- Render a chart for a specific Kubernetes version:

`helm template {{release_name}} {{repository_name}}/{{chart_name}} --kube-version {{kubernetes_version}}`
