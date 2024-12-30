# ccache

> C/C++ 编译器缓存。
> 注意：软件包通常在 `/usr/lib/ccache/bin` 中提供编译器的符号链接。将此目录添加到 `$PATH` 中，以自动对它们使用 `ccache`。
> 更多信息：<https://ccache.dev/manual/latest.html>。

- 显示当前缓存 [s]tatistics：

`ccache --show-stats`

- [C]lear 所有缓存：

`ccache --clear`

- 重置 ([z]ero) 统计信息（但不清除缓存本身）：

`ccache --zero-stats`

- 编译 C 代码并缓存编译输出（要在所有 `gcc` 调用中使用 `ccache`，请参见上面的说明）：

`ccache gcc {{path/to/file.c}}`