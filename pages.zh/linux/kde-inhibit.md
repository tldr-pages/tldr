# kde-inhibit

> 在命令运行时抑制各种桌面功能。
> 更多信息：<https://invent.kde.org/plasma/kde-cli-tools/-/blob/master/kdeinhibit/main.cpp>.

- 抑制电源管理：

`kde-inhibit --power {{command}} {{command_arguments}}`

- 抑制屏幕保护程序：

`kde-inhibit --screenSaver {{command}} {{command_arguments}}`

- 启动 VLC，并在运行时抑制颜色校正（夜间模式）：

`kde-inhibit --colorCorrect {{vlc}}`
