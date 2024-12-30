# fprintd-verify

> 验证指纹与数据库中的记录。
> 更多信息：<https://manned.org/fprintd-verify>。

- 验证当前用户的所有存储指纹：

`fprintd-verify`

- 验证当前用户的特定指纹：

`fprintd-verify --finger {{左拇指|左食指|左中指|左无名指|左小指|右拇指|右食指|右中指|右无名指|右小指}}`

- 验证特定用户的指纹：

`fprint-verify {{用户名}}`

- 验证特定用户的特定指纹：

`fprintd-verify --finger {{指纹名称}} {{用户名}}`

- 如果指纹与当前用户数据库中存储的指纹不匹配，则使过程失败：

`fprint-verify --g-fatal-warnings`

- 显示帮助信息：

`fprintd-verify --help`