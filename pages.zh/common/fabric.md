# fabric

> 一个使用 AI 增强人类的开源框架。
> 提供了一个模块化框架，用于使用众包的一套 AI 提示来解决特定问题。
> 更多信息：<https://github.com/danielmiessler/fabric>.

- 运行设置以配置 fabric：

`fabric --setup`

- 列出所有可用的模式：

`fabric --listpatterns`

- 从文件读取输入运行模式：

`fabric --pattern {{pattern_name}} < {{path/to/input_file}}`

- 在 YouTube 视频 URL 上运行模式：

`fabric --youtube "{{https://www.youtube.com/watch?v=video_id}}" --pattern {{pattern_name}}`

- 通过管道连接多个模式：

`fabric --pattern {{pattern1}} | fabric --pattern {{pattern2}}`

- 运行自定义用户定义的模式：

`fabric --pattern {{custom_pattern_name}}`

- 运行模式并将输出保存到文件：

`fabric --pattern {{pattern_name}} --output {{path/to/output_file}}`

- 使用指定的变量运行模式：

`fabric --pattern {{pattern_name}} --variable "{{variable_name}}:{{value}}"`