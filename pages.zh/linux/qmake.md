# qmake

> 从 Qt 项目文件生成 Makefile。
> 更多信息：<https://doc.qt.io/qt-6/qmake-manual.html>。

- 从当前目录中的项目文件生成 `Makefile`：

`qmake`

- 指定 `Makefile` 和项目文件的位置：

`qmake -o {{path/to/Makefile}} {{path/to/project_file.pro}}`

- 生成默认的项目文件：

`qmake -project`

- 编译项目：

`qmake && make`

- 启用调试模式：

`qmake -d`

- 显示帮助：

`qmake -help`
