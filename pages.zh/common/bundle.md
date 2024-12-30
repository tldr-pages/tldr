# bundle

> Ruby编程语言的依赖管理工具。
> 更多信息: <https://bundler.io/man/bundle.1.html>。

- 安装工作目录中`Gemfile`中定义的所有gem：

`bundle install`

- 在当前bundle的上下文中执行命令：

`bundle exec {{command}} {{arguments}}`

- 按照`Gemfile`中定义的规则更新所有gem，并重新生成`Gemfile.lock`：

`bundle update`

- 更新`Gemfile`中定义的一个或多个特定gem：

`bundle update {{gem_name1}} {{gem_name2}}`

- 更新`Gemfile`中定义的一个或多个特定gem，但仅更新到下一个补丁版本：

`bundle update --patch {{gem_name1}} {{gem_name2}}`

- 更新`Gemfile`中给定组内的所有gem：

`bundle update --group {{development}}`

- 列出已安装的gem，并查看可用的更新版本：

`bundle outdated`

- 创建一个新的gem骨架：

`bundle gem {{gem_name}}`