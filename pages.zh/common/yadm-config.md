# yadm-config

> 向 `yadm` 的配置文件传递选项。更改由 `yadm` 管理的存储库的 `.config`。
> 更多信息：<https://github.com/TheLocehiliosan/yadm/blob/master/yadm.md#configuration>。

- 设置或更新 `yadm` 的 Git 配置：

`yadm config {{key.inner-key}} {{value}}`

- 从 `yadm` 的 Git 配置中获取一个值：

`yadm config --get {{key}}`

- 在 `yadm` 的 Git 配置中取消设置一个值：

`yadm config --unset {{key}}`

- 列出 `yadm` 的 Git 配置中的所有值：

`yadm config --list`