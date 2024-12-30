# ruby

> Ruby 编程语言解释器。
> 另见：`gem`，`bundler`，`rake`，`irb`。
> 更多信息：<https://www.ruby-lang.org>。

- 执行一个 Ruby 脚本：

`ruby {{script.rb}}`

- 在命令行中执行一个 Ruby 命令：

`ruby -e {{command}}`

- 检查给定 Ruby 脚本的语法错误：

`ruby -c {{script.rb}}`

- 在当前目录下的 8080 端口启动内置 HTTP 服务器：

`ruby -run -e httpd`

- 在不安装所需库的情况下本地执行 Ruby 二进制文件：

`ruby -I {{path/to/library_folder}} -r {{library_require_name}} {{path/to/bin_folder/bin_name}}`

- 显示 Ruby 版本：

`ruby -v`