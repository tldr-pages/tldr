# kscreen-doctor

> 更改和操作屏幕设置。
> 更多信息：<https://invent.kde.org/plasma/libkscreen>。

- 显示输出信息：

`kscreen-doctor --outputs`

- 将 ID 为 1 的显示输出的旋转设置为右：

`kscreen-doctor {{output.1.rotation.right}}`

- 将 ID 为 `HDMI-2` 的显示输出的缩放设置为 2（200%）：

`kscreen-doctor {{output.HDMI-2.scale.2}}`