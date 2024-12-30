# fabric

> 一个用于增强人类与AI结合的开源框架。
> 提供一个模块化框架，用于使用众包的AI提示解决特定问题。
> 更多信息请访问：<https://github.com/danielmiessler/fabric>。

- 运行设置以配置fabric：

`fabric --setup`

- 列出所有可用的模式：

`fabric --listpatterns`

- 从文件中运行模式：

`fabric --pattern {{pattern_name}} < {{path/to/input_file}}`

- 在YouTube视频URL上运行模式：

`fabric --youtube "{{https://www.youtube.com/watch?v=video_id}}" --pattern {{pattern_name}}`

- 通过将一个模式的输出连接到另一个模式来链接模式：

`fabric --pattern {{pattern1}} | fabric --pattern {{pattern2}}`

- 运行自定义用户定义的模式：

`fabric --pattern {{custom_pattern_name}}`

- 运行模式并将输出保存到文件：

`fabric --pattern {{pattern_name}} --output {{path/to/output_file}}`

- 运行模式并指定变量：

`fabric --pattern {{pattern_name}} --variable "{{variable_name}}:{{value}}"`