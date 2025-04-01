# md-to-clip

> 将 tldr 页面转换为命令行接口页面。
> 参见：`clip-view`。
> 更多信息：<https://github.com/command-line-interface-pages/v2-tooling/tree/main/md-to-clip>。

- 转换 tldr 页面文件并保存到同一目录：

`md-to-clip {{path/to/page1.md path/to/page2.md ...}}`

- 转换 tldr 页面文件并保存到指定目录：

`md-to-clip --output-directory {{path/to/directory}} {{path/to/page1.md path/to/page2.md ...}}`

- 将 tldr 页面文件转换为 `stdout`：

`md-to-clip --no-file-save <(echo '{{page-content}}')`

- 转换 tldr 页面文件时，使用特定配置文件中的额外占位符：

`md-to-clip --special-placeholder-config {{path/to/config.yaml}} {{path/to/page1.md path/to/page2.md ...}}`

- 显示帮助信息：

`md-to-clip --help`

- 显示版本信息：

`md-to-clip --version`