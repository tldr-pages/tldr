# md-to-clip

> 将 tldr-pages 转换为命令行接口页面。
> 另见：`clip-view`。
> 更多信息：<https://github.com/command-line-interface-pages/v2-tooling/tree/main/md-to-clip>。

- 转换 tldr-pages 文件并保存到相同目录：

`md-to-clip {{path/to/page1.md path/to/page2.md ...}}`

- 转换 tldr-pages 文件并保存到特定目录：

`md-to-clip --output-directory {{path/to/directory}} {{path/to/page1.md path/to/page2.md ...}}`

- 将 tldr-page 文件转换为 `stdout`：

`md-to-clip --no-file-save <(echo '{{page-content}}')`

- 在转换 tldr-pages 文件时识别来自特定配置的额外占位符：

`md-to-clip --special-placeholder-config {{path/to/config.yaml}} {{path/to/page1.md path/to/page2.md ...}}`

- 显示帮助：

`md-to-clip --help`

- 显示版本：

`md-to-clip --version`