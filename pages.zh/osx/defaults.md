# defaults

> 读取和写入 macOS 应用程序的用户配置。
> 更多信息：<https://keith.github.io/xcode-man-pages/defaults.1.html>.

- 读取应用程序选项的系统默认值：

`defaults read {{应用名}} {{选项}}`

- 读取应用程序选项的默认值：

`defaults read -app {{应用名}} {{选项}}`

- 写入应用程序选项的默认值：

`defaults write {{应用名}} {{选项}} {{- 类型}} {{值}}`

- 加速任务控制界面弹出动画（时间设置为 0.1）：

`defaults write com.apple.Dock expose-animation-duration -float 0.1`

- 删除应用程序的所有默认值：

`defaults delete {{应用名}}`
