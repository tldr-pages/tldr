# bosh

> 部署和管理 BOSH 调度器。
> 更多信息：<https://bosh.io/docs/cli-v2/>.

- 为特定环境中的调度器创建本地别名：

`bosh alias-env {{environment_name}} {{[-e|--environment]}} {{ip_address|URL}} --ca-cert {{ca_certificate}}`

- 列出环境：

`bosh environments`

- 登录调度器：

`bosh login {{[-e|--environment]}} {{environment}}`

- 列出部署：

`bosh {{[-e|--environment]}} {{environment}} deployments`

- 列出部署中的环境虚拟机：

`bosh {{[-e|--environment]}} {{environment}} vms {{[-d|--deployment]}} {{deployment}}`

- 通过 SSH 连接到虚拟机：

`bosh {{[-e|--environment]}} {{environment}} ssh {{virtual_machine}} {{[-d|--deployment]}} {{deployment}}`

- 上传 stemcell：

`bosh {{[-e|--environment]}} {{environment}} upload-stemcell {{stemcell_file|url}}`

- 显示当前的云配置：

`bosh {{[-e|--environment]}} {{environment}} cloud-config`
