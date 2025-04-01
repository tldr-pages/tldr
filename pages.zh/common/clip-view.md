# clip-view

> 命令行接口页面渲染工具。
> 用于类似 TLDR 的项目，支持更广泛的语法和多种渲染模式。
> 更多信息：<https://github.com/command-line-interface-pages/v2-tooling/tree/main/clip-view>.

- 渲染特定的本地页面：

`clip-view {{path/to/page1.clip path/to/page2.clip ...}}`

- 渲染特定的远程页面：

`clip-view {{page_name1 page_name2 ...}}`

- 通过特定渲染器渲染页面：

`clip-view --render {{tldr|tldr-colorful|docopt|docopt-colorful}} {{page_name1 page_name2 ...}}`

- 使用特定颜色主题渲染页面：

`clip-view --theme {{path/to/local_theme.yaml|remote_theme_name}} {{page_name1 page_name2 ...}}`

- 清除页面或主题缓存：

`clip-view --clear-{{page|theme}}-cache`

- 显示帮助信息：

`clip-view --help`

- 显示版本信息：

`clip-view --version`
