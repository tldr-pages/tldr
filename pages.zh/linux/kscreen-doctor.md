# kscreen-doctor

> 更改和操作屏幕设置。
> 更多信息：<https://invent.kde.org/plasma/libkscreen>。

- 显示输出信息：

`kscreen-doctor --outputs`

- 将 ID 为 1 的显示输出旋转到右侧：

`kscreen-doctor {{output.1.rotation.right}}`

- 将 ID 为 `HDMI-2` 的显示输出缩放设置为 2（200%）：

`kscreen-doctor {{output.HDMI-2.scale.2}}`
