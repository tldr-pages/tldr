# pulumi new

> 创建一个新的 Pulumi 项目。
> 更多信息：<https://www.pulumi.com/docs/iac/cli/commands/pulumi_new/>.

- 交互式选择模板：

`pulumi new`

- 从特定模板创建项目（例如 `azure-python`）：

`pulumi new {{provided-template}}`

- 从本地文件创建项目：

`pulumi new {{path/to/templates/aws-typescript}}`

- 从 Git 仓库创建项目：

`pulumi new {{url}}`

- 使用指定的密钥提供者与 <pulumi.com> 后端配合使用：

`pulumi new --secrets-provider={{passphrase}}`
