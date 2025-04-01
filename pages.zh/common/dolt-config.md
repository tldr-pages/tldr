# dolt config

> 读取和写入本地（每个存储库）和全局（每个用户）Dolt 配置变量。
> 更多信息：<https://docs.dolthub.com/cli-reference/cli#dolt-config>。

- 列出所有本地和全局配置选项及其值：

`dolt config --list`

- 显示本地或全局配置变量的值：

`dolt config --get {{name}}`

- 修改本地配置变量的值，如果变量不存在则创建它：

`dolt config --add {{name}} {{value}}`

- 修改全局配置变量的值，如果变量不存在则创建它：

`dolt config --global --add {{name}} {{value}}`

- 删除本地配置变量：

`dolt config --unset {{name}}`

- 删除全局配置变量：

`dolt config --global --unset {{name}}`