# helm upgrade

> Upgrade a helm release to a new version of a chart or with new configuration.
> More information: <https://helm.sh/docs/helm/helm_upgrade/>.

- Upgrade a release to the latest version of a chart:

`helm upgrade {{release_name}} {{repository_name}}/{{chart_name}}`

- Upgrade a release from an unpacked chart directory:

`helm upgrade {{release_name}} {{path/to/source_directory}}`

- Upgrade a release, or install it if it does not exist yet:

`helm upgrade {{[-i|--install]}} {{release_name}} {{repository_name}}/{{chart_name}}`

- Upgrade a release to a specific chart version:

`helm upgrade {{release_name}} {{repository_name}}/{{chart_name}} --version {{chart_version}}`

- Upgrade a release in a specific namespace:

`helm upgrade {{release_name}} {{repository_name}}/{{chart_name}} {{[-n|--namespace]}} {{namespace}}`

- Upgrade a release with custom values:

`helm upgrade {{release_name}} {{repository_name}}/{{chart_name}} --set {{parameter1}}={{value1}},{{parameter2}}={{value2}}`

- Upgrade a release passing a custom values file:

`helm upgrade {{release_name}} {{repository_name}}/{{chart_name}} {{[-f|--values]}} {{path/to/values.yaml}}`

- Simulate an upgrade without actually doing it:

`helm upgrade {{release_name}} {{repository_name}}/{{chart_name}} --dry-run`
