# gem

> Ruby 编程语言的包管理器。
> 更多信息：<https://guides.rubygems.org>。

- 搜索远程 gem(s) 并显示所有可用版本：

`gem search {{正则表达式}} --all`

- 安装 gem 的最新版本：

`gem install {{gem_name}}`

- 安装 gem 的特定版本：

`gem install {{gem_name}} --version {{1.0.0}}`

- 安装 gem 的最新匹配版本（语义版本）：

`gem install {{gem_name}} --version '~> {{1.0}}'`

- 更新 gem：

`gem update {{gem_name}}`

- 列出所有本地 gem：

`gem list`

- 卸载 gem：

`gem uninstall {{gem_name}}`

- 卸载 gem 的特定版本：

`gem uninstall {{gem_name}} --version {{1.0.0}}`
