# tlmgr gui

> 启动 `tlmgr` 的图形用户界面。
> `tlmgr gui` 依赖于手动安装的 `perl-tk` 包。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 启动 `tlmgr` 的 GUI：

`sudo tlmgr gui`

- 启动 GUI 并指定背景颜色：

`sudo tlmgr gui -background "{{#f39bc3}}"`

- 启动 GUI 并指定前景颜色：

`sudo tlmgr gui -foreground "{{#0ef3bd}}"`

- 启动 GUI 并指定字体和字体大小：

`sudo tlmgr gui -font "{{helvetica 18}}"`

- 启动 GUI 并设置特定的几何形状：

`sudo tlmgr gui -geometry {{width}}x{{height}}-{{xpos}}+{{ypos}}`

- 启动 GUI 并传递任意的 X 资源字符串：

`sudo tlmgr gui -xrm {{xresource}}`