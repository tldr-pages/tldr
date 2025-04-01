# bundle

> Ruby 编程语言的依赖管理器。
> 更多信息：<https://bundler.io/man/bundle.1.html>.

- 安装 `Gemfile` 中定义的所有 gem，该文件应位于工作目录中：

`bundle install`

- 在当前 bundle 的上下文中执行命令：

`bundle exec {{command}} {{arguments}}`

- 根据 `Gemfile` 中的规则更新所有 gem 并重新生成 `Gemfile.lock`：

`bundle update`

- 更新 `Gemfile` 中定义的一个或多个指定 gem：

`bundle update {{gem_name1}} {{gem_name2}}`

- 更新 `Gemfile` 中定义的一个或多个指定 gem，但仅升级到下一个补丁版本：

`bundle update --patch {{gem_name1}} {{gem_name2}}`

- 更新 `Gemfile` 中指定组内的所有 gem：

`bundle update --group {{development}}`

- 列出 `Gemfile` 中已安装且有更新版本可用的 gem：

`bundle outdated`

- 创建一个新的 gem 模板：

`bundle gem {{gem_name}}`