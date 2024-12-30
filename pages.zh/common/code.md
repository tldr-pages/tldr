# 代码

> 跨平台且可扩展的代码编辑器。
> 更多信息：<https://github.com/microsoft/vscode>。

- 启动 Visual Studio Code：

`code`

- 打开特定文件/目录：

`code {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 比较两个特定文件：

`code --diff {{path/to/file1}} {{path/to/file2}}`

- 在新窗口中打开特定文件/目录：

`code --new-window {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 安装/卸载特定扩展：

`code --{{install|uninstall}}-extension {{publisher.extension}}`

- 打印已安装的扩展：

`code --list-extensions`

- 打印已安装的扩展及其版本：

`code --list-extensions --show-versions`

- 以超级用户（root）身份启动编辑器，同时将用户数据存储在特定目录中：

`sudo code --user-data-dir {{path/to/directory}}`