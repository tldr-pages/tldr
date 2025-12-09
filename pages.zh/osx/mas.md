# mas

> Mac 应用商店的命令行界面。
> 更多信息：<https://github.com/mas-cli/mas>.

- 首次登录 Mac 应用商店：

`mas signin "{{user@example.com}}"`

- 显示所有已安装的应用程序和它们的产品标识符：

`mas list`

- 搜索一个应用程序，在结果旁边显示价格：

`mas search "{{应用程序}}" --price`

- 安装或更新一个应用程序：

`mas install {{产品标识符}}`

- 安装所有待定的更新：

`mas upgrade`
