# gem

> Ruby 编程语言的包管理器。
> 更多信息：<https://guides.rubygems.org>。

- 搜索远程 gem 并显示所有可用版本：

`gem search {{正则表达式}} --all`

- 安装 gem 的最新版本：

`gem install {{gem_name}}`

- 安装特定版本的 gem：

`gem install {{gem_name}} --version {{1.0.0}}`

- 安装最新匹配的 (SemVer) 版本的 gem：

`gem install {{gem_name}} --version '~> {{1.0}}'`

- 更新一个 gem：

`gem update {{gem_name}}`

- 列出所有本地 gem：

`gem list`

- 卸载一个 gem：

`gem uninstall {{gem_name}}`

- 卸载特定版本的 gem：

`gem uninstall {{gem_name}} --version {{1.0.0}}`