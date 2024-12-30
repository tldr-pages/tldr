# defaults

> 读取和写入 macOS 应用程序的用户配置。
> 更多信息：<https://keith.github.io/xcode-man-pages/defaults.1.html>。

- 读取应用程序选项的系统默认值：

`defaults read "{{application}}" "{{option}}"`

- 读取应用程序选项的默认值：

`defaults read -app "{{application}}" "{{option}}"`

- 在域名、键和值中搜索关键字：

`defaults find "{{keyword}}"`

- 写入应用程序选项的默认值：

`defaults write "{{application}}" "{{option}}" {{-type}} {{value}}`

- 加快 Mission Control 动画速度：

`defaults write com.apple.Dock expose-animation-duration -float 0.1`

- 删除应用程序的所有默认值：

`defaults delete "{{application}}"`