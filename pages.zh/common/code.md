# code

> 跨平台且可扩展的代码编辑器。
> 更多信息：<https://code.visualstudio.com/docs/configure/command-line>.

- 启动 Visual Studio Code：

`code`

- 打开指定的文件或目录：

`code {{路径/到/文件或目录1 路径/到/文件或目录2 ...}}`

- 比较两个指定的文件：

`code {{[-d|--diff]}} {{路径/到/文件1}} {{路径/到/文件2}}`

- 在新窗口中打开指定的文件或目录：

`code {{[-n|--new-window]}} {{路径/到/文件或目录1 路径/到/文件或目录2 ...}}`

- 安装/卸载一个特定的插件：

`code --{{install|uninstall}}-extension {{插件作者.插件名}}`

- 输出已安装的插件：

`code --list-extensions`

- 输出已安装的插件及其版本：

`code --list-extensions --show-versions`

- 以超级用户（root）身份启动编辑器，同时将用户数据存储在指定目录中：

`sudo code --user-data-dir {{路径/到/目录}}`
