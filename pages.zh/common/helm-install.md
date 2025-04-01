# helm install

> 安装 Helm 图表。
> 更多信息：<https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package>.

- 安装 Helm 图表：

`helm install {{name}} {{repository_name}}/{{chart_name}}`

- 从已解包的图表目录安装 Helm 图表：

`helm install {{name}} {{path/to/source_directory}}`

- 从 URL 安装 Helm 图表：

`helm install {{package_name}} {{https://example.com/charts/packagename-1.2.3.tgz}}`

- 安装 Helm 图表并自动生成名称：

`helm install {{repository_name}}/{{chart_name}} --generate-name`

- 执行干运行（模拟安装）：

`helm install {{name}} {{repository_name}}/{{chart_name}} --dry-run`

- 使用自定义值安装 Helm 图表：

`helm install {{name}} {{repository_name}}/{{chart_name}} --set {{parameter1}}={{value1}},{{parameter2}}={{value2}}`

- 使用自定义值文件安装 Helm 图表：

`helm install {{name}} {{repository_name}}/{{chart_name}} --values {{path/to/values.yaml}}`
