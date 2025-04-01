# glib-compile-resources

> 将资源文件（如图片）编译成二进制资源包。
> 这些资源可以使用 GResource API 链接到 GTK 应用程序中。
> 更多信息：<https://manned.org/glib-compile-resources>。

- 将 `file.gresource.xml` 中引用的资源编译为 .gresource 二进制文件：

`glib-compile-resources {{file.gresource.xml}}`

- 将 `file.gresource.xml` 中引用的资源编译为 C 源文件：

`glib-compile-resources --generate-source {{file.gresource.xml}}`

- 将 `file.gresource.xml` 中的资源编译为指定的目标文件，扩展名可以是 .c、.h 或 .gresource：

`glib-compile-resources --generate --target={{file.ext}} {{file.gresource.xml}}`

- 打印 `file.gresource.xml` 中引用的所有资源文件列表：

`glib-compile-resources --generate-dependencies {{file.gresource.xml}}`