# qmake

> 从 Qt 项目文件生成 Makefile。
> 更多信息：<https://doc.qt.io/qt-6/qmake-running.html>。

- 从当前目录中的项目文件生成一个 `Makefile`：

`qmake`

- 指定 `Makefile` 和项目文件的位置：

`qmake -o {{路径/到/Makefile}} {{路径/到/项目文件.pro}}`

- 生成一个默认的项目文件：

`qmake -project`

- 编译一个项目：

`qmake && make`

- 启用调试模式：

`qmake -d`

- 显示帮助：

`qmake -help`
