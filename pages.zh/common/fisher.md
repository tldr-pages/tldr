# fisher

> Fisher，一个fish shell插件管理器。
> 通过名称或从管理的'fishfile'中安装插件以进行打包安装。
> 更多信息：<https://github.com/jorgebucaran/fisher>。

- 安装一个或多个插件：

`fisher {{plugin1}} {{plugin2}}`

- 从GitHub gist安装插件：

`fisher {{gist_url}}`

- 使用您喜欢的编辑器手动编辑'fishfile'并安装多个插件：

`{{editor}} ~/.config/fish/fishfile; fisher`

- 列出已安装的插件：

`fisher ls`

- 更新插件：

`fisher update`

- 移除一个或多个插件：

`fisher remove {{plugin1}} {{plugin2}}`