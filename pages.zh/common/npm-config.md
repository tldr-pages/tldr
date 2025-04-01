# npm-config

> 管理 `npm` 配置设置。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-config>.

- 显示所有配置设置：

`npm config list`

- 以 `JSON` 格式列出所有配置设置：

`npm config list --json`

- 获取特定配置键的值：

`npm config get {{key}}`

- 将配置键设置为特定值：

`npm config set {{key}}={{value}}`

- 删除配置键：

`npm config delete {{key}}`

- 使用默认编辑器编辑全球 npm 配置文件：

`npm config edit`

- 尝试修复无效的配置项：

`npm config fix`
