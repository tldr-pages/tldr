# zapier 构建

> 构建一个可推送的 `zip` 文件，用于 Zapier 集成。
> 更多信息：<https://platform.zapier.com/reference/cli#build>。

- 创建构建：

`zapier build`

- 禁用智能文件包含（只会包含 `index.js` 所需的文件）：

`zapier build --disable-dependency-detection`

- 显示额外的调试输出：

`zapier build {{-d|--debug}}`