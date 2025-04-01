# rake

> 类似于 Make 的 Ruby 程序。
> `rake` 的任务在 Rakefile 中指定。
> 更多信息：<https://ruby.github.io/rake>.

- 运行 Rakefile 中的 `default` 任务：

`rake`

- 运行特定任务：

`rake {{task}}`

- 并行执行 `n` 个任务（默认为 CPU 核心数 + 4）：

`rake --jobs {{n}}`

- 使用特定的 Rakefile：

`rake --rakefile {{path/to/Rakefile}}`

- 从其他目录执行 `rake`：

`rake --directory {{path/to/directory}}`