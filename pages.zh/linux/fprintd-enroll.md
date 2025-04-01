# fprintd-enroll

> 将指纹注册到数据库中。
> 更多信息：<https://manned.org/fprintd-enroll>。

- 为当前用户注册右食指：

`fprintd-enroll`

- 为当前用户注册特定的手指：

`fprintd-enroll --finger {{left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|right-index-finger|right-middle-finger|right-ring-finger|right-little-finger}}`

- 为特定用户注册右食指：

`fprintd-enroll {{username}}`

- 为特定用户注册特定的手指：

`fprintd-enroll --finger {{finger_name}} {{username}}`

- 显示帮助：

`fprintd-enroll --help`
