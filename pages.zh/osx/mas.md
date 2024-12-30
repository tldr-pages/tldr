# mas

> Mac 应用商店的命令行界面。
> 更多信息：<https://github.com/mas-cli/mas>。

- 第一次登录 Mac 应用商店：

`mas signin "{{user@example.com}}"`

- 显示所有已安装的应用程序及其产品标识符：

`mas list`

- 搜索应用程序，并在结果中显示价格：

`mas search "{{application}}" --price`

- 使用确切的数字 ID 安装或更新应用程序：

`mas install {{numeric_product_id}}`

- 安装搜索结果中返回的第一个应用程序：

`mas lucky "{{search_term}}"`

- 列出所有有待更新的过时应用程序：

`mas outdated`

- 安装所有待处理的更新：

`mas upgrade`

- 更新特定应用程序：

`mas upgrade "{{numeric_product_id}}"`