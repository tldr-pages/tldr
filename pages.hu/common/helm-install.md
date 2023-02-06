# helm install

> Kormánytérkép telepítése. További információ: <https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package>.

- Kormánytérkép telepítése:

`helm install {{name}} {{repository_name}}/{{chart_name}}`

- Telepítsen egy kormánytérképet egy kicsomagolt térképkönyvtárból:

`helm install {{name}} {{path/to/source_directory}}`

- Kormánytérkép telepítése URL-címről:

`helm install {{package_name}} {{https://example.com/charts/packagename-1.2.3.tgz}}`

- Kormánytérkép telepítése és nevének generálása:

`helm install {{repository_name}}/{{chart_name}} --generate-name`

- Száraz futtatás végrehajtása:

`helm install {{name}} {{repository_name}}/{{chart_name}} --dry-run`

- Kormánytérkép telepítése egyéni értékekkel:

`helm install {{name}} {{repository_name}}/{{chart_name}} --set {{parameter1}}={{value1}},{{parameter2}}={{value2}}`

- Egyéni értékfájl átadása a kormánytérkép telepítéséhez:

`helm install {{name}} {{repository_name}}/{{chart_name}} --values {{path/to/values.yaml}}`
