# tlmgr gui

> 启动 `tlmgr` 的图形用户界面。
> `tlmgr gui` 依赖于 `perl-tk` 包，需要手动安装。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>.

- 启动 `tlmgr` 的图形界面：

`sudo tlmgr gui`

- 指定背景颜色启动图形界面：

`sudo tlmgr gui -background "{{#f39bc3}}"`

- 指定前景颜色启动图形界面：

`sudo tlmgr gui -foreground "{{#0ef3bd}}"`

- 指定字体和字体大小启动图形界面：

`sudo tlmgr gui -font "{{helvetica 18}}"`

- 设置特定的几何尺寸启动图形界面：

`sudo tlmgr gui -geometry {{width}}x{{height}}-{{xpos}}+{{ypos}}`

- 传递一个任意的 X 资源字符串启动图形界面：

`sudo tlmgr gui -xrm {{xresource}}`