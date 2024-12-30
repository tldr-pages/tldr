# bosh

> 部署和管理 BOSH 指挥官。
> 更多信息： <https://bosh.io/docs/cli-v2/>。

- 在特定的 [e]nvironment 中为指挥官创建本地别名：

`bosh alias-env {{environment_name}} -e {{ip_address|URL}} --ca-cert {{ca_certificate}}`

- 列出环境：

`bosh environments`

- 登录到指挥官：

`bosh login -e {{environment}}`

- 列出部署：

`bosh -e {{environment}} deployments`

- 列出部署中的环境虚拟机：

`bosh -e {{environment}} vms -d {{deployment}}`

- SSH 登录虚拟机：

`bosh -e {{environment}} ssh {{virtual_machine}} -d {{deployment}}`

- 上传 stemcell：

`bosh -e {{environment}} upload-stemcell {{stemcell_file|url}}`

- 显示当前云配置：

`bosh -e {{environment}} cloud-config`