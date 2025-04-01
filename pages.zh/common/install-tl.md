# install-tl

> TeX Live 跨平台安装程序。
> 更多信息：<https://tug.org/texlive/>.

- 启动基于文本的安装程序（Unix 系统默认）：

`install-tl -no-gui`

- 启动图形用户界面安装程序（macOS 和 Windows 默认，需要 Tcl/Tk）：

`install-tl -gui`

- 根据特定配置文件安装 TeX Live：

`install-tl -profile {{path/to/texlive.profile}}`

- 使用特定配置文件中的设置启动安装程序：

`install-tl -init-from-file {{path/to/texlive.profile}}`

- 启动安装程序以在便携设备（如 U 盘）上安装：

`install-tl -portable`

- 显示帮助：

`install-tl -help`
