# gummy

> 用于 Linux/X11 的屏幕亮度和色温管理工具。
> 更多信息：<https://github.com/Gitoffthelawn/gummy>。

- 将屏幕色温设置为 3000K：

`gummy --temperature {{3000}}`

- 将屏幕背光设置为 50%：

`gummy --backlight {{50}}`

- 将屏幕像素亮度设置为 45%：

`gummy --brightness {{45}}`

- 将当前屏幕像素亮度增加 10%：

`gummy --brightness {{+10}}`

- 将当前屏幕像素亮度减少 10%：

`gummy --brightness {{-10}}`

- 为第二个屏幕设置色温和像素亮度：

`gummy --screen {{1}} --temperature {{3800}} --brightness {{65}}`
