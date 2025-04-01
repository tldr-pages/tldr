# pkg-config

> 提供编译应用程序所需已安装库的详细信息。
> 更多信息：<https://www.freedesktop.org/wiki/Software/pkg-config/>.

- 获取库及其依赖项的列表：

`pkg-config --libs {{library1 library2 ...}}`

- 获取库、其依赖项以及适用于 gcc 的正确 cflags 列表：

`pkg-config --cflags --libs {{library1 library2 ...}}`

- 编译你的代码，使用 libgtk-3、libwebkit2gtk-4.0 及其所有依赖项：

`c++ example.cpp $(pkg-config --cflags --libs gtk+-3.0 webkit2gtk-4.0) -o example`