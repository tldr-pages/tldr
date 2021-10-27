# helm install

> Install a helm chart.
> More information: <https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package>.

- Install a helm chart:

`helm install {{name}} {{repository_name}}/{{chart_name}}`

- Install a helm chart from an unpacked chart directory:

`helm install {{name}} {{path/to/source_directory}}`

- Install a helm chart from a URL:

`helm install {{mynginx}} {{https://example.com/charts/nginx-1.2.3.tgz}}`

- Install a helm chart and generate a name:

`helm install {{repository_name}}/{{chart_name}} --generate-name`

- Perform a dry run:

`helm install {{name}} {{repository_name}}/{{chart_name}} --dry-run`

- Install a helm chart with custom values:

`helm install {{name}} {{repository_name}}/{{chart_name}} --set {{parameter1}}={{value1}},{{parameter2}}={{value2}}`

- Install a helm chart passing a values file:

`helm install {{name}} {{repository_name}}/{{chart_name}} --values {{path/to/values.yaml}}`
