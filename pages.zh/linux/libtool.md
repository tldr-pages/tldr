# libtool

> 一个通用的库支持脚本，用于隐藏使用共享库的复杂性，提供一个一致且可移植的接口。
> 更多信息：<https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtool>.

- 将源文件编译成 `libtool` 对象：

`libtool --mode=compile gcc {{[-c|--compile]}} {{path/to/source.c}} {{[-o|--output]}} {{path/to/source.lo}}`

- 创建库或可执行文件：

`libtool --mode=link gcc {{[-o|--output]}} {{path/to/library.lo}} {{path/to/source.lo}}`

- 自动设置库路径，以便其他程序可以使用未安装的 `libtool` 生成的程序或库：

`libtool --mode=execute gdb {{path/to/program}}`

- 安装共享库：

`libtool --mode=install cp {{path/to/library.la}} {{path/to/installation_directory}}`

- 完成系统上 `libtool` 库的安装：

`libtool --mode=finish {{path/to/installation_dir}}`

- 删除已安装的库或可执行文件：

`libtool --mode=uninstall {{path/to/installed_library.la}}`

- 删除未安装的库或可执行文件：

`libtool --mode=clean rm {{path/to/source.lo}} {{path/to/library.la}}`