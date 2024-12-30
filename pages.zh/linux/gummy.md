# gummy

> Linux/X11 的屏幕亮度/温度管理器。
> 更多信息: <https://github.com/Gitoffthelawn/gummy>。

- 将屏幕温度设置为 3000K：

`gummy --temperature {{3000}}`

- 将屏幕背光设置为 50%：

`gummy --backlight {{50}}`

- 将屏幕像素亮度设置为 45%：

`gummy --brightness {{45}}`

- 将当前屏幕像素亮度提高 10%：

`gummy --brightness {{+10}}`

- 将当前屏幕像素亮度降低 10%：

`gummy --brightness {{-10}}`

- 为第二个屏幕设置温度和像素亮度：

`gummy --screen {{1}} --temperature {{3800}} --brightness {{65}}`