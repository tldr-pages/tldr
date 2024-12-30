# install-tl

> TeX Live 跨平台安装程序。
> 更多信息：<https://tug.org/texlive/>.

- 启动基于文本的安装程序（在Unix系统上默认）：

`install-tl -no-gui`

- 启动图形用户界面安装程序（在macOS和Windows上默认，需要Tcl/Tk）：

`install-tl -gui`

- 根据特定配置文件安装TeX Live：

`install-tl -profile {{path/to/texlive.profile}}`

- 使用特定配置文件中的设置启动安装程序：

`install-tl -init-from-file {{path/to/texlive.profile}}`

- 启动便携设备（如USB闪存驱动器）上的安装程序：

`install-tl -portable`

- 显示帮助信息：

`install-tl -help`