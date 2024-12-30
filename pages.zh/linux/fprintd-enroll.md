# fprintd-enroll

> 将指纹注册到数据库中。
> 更多信息：<https://manned.org/fprintd-enroll>。

- 为当前用户注册右食指：

`fprintd-enroll`

- 为当前用户注册特定手指：

`fprintd-enroll --finger {{左大拇指|左食指|左中指|左无名指|左小拇指|右大拇指|右食指|右中指|右无名指|右小拇指}}`

- 为特定用户注册右食指：

`fprintd-enroll {{用户名}}`

- 为特定用户注册特定手指：

`fprintd-enroll --finger {{手指名称}} {{用户名}}`

- 显示帮助信息：

`fprintd-enroll --help`