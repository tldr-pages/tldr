# fprintd-verify

> 验证数据库中的指纹。
> 更多信息：<https://manned.org/fprintd-verify>。

- 验证当前用户的所有存储指纹：

`fprintd-verify`

- 验证当前用户的特定指纹：

`fprintd-verify --finger {{left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|right-index-finger|right-middle-finger|right-ring-finger|right-little-finger}}`

- 验证特定用户的所有指纹：

`fprint-verify {{username}}`

- 验证特定用户的特定指纹：

`fprintd-verify --finger {{finger_name}} {{username}}`

- 如果当前用户的指纹与数据库中的指纹不匹配，则使过程失败：

`fprint-verify --g-fatal-warnings`

- 显示帮助信息：

`fprintd-verify --help`
