# pkg-config

> 提供用于编译应用程序的已安装库的详细信息。
> 更多信息：<https://www.freedesktop.org/wiki/Software/pkg-config/>.

- 获取库及其依赖项的列表：

`pkg-config --libs {{library1 library2 ...}}`

- 获取库、它们的依赖项和适用于gcc的正确cflags的列表：

`pkg-config --cflags --libs {{library1 library2 ...}}`

- 使用libgtk-3、libwebkit2gtk-4.0及其所有依赖项编译代码：

`c++ example.cpp $(pkg-config --cflags --libs gtk+-3.0 webkit2gtk-4.0) -o example`