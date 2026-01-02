# choco list

> 使用 Chocolatey 显示包列表。
> 更多信息：<https://docs.chocolatey.org/en-us/choco/commands/list/>。

- 列出所有可用的包：
  choco list

- 列出所有本地已安装的包：
  choco list --local-only

- 显示包含本地程序的列表：
  choco list --include-programs

- 仅显示已批准的包：
  choco list --approved-only

- 从指定的源显示包：
  choco list --source {{源_URL|别名}}

- 提供用户名和密码进行身份验证：
  choco list --user {{用户名}} --password {{密码}}