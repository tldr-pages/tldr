# ccache

> C/C++ 编译器缓存。
> 注意：通常包会为编译器在 `/usr/lib/ccache/bin` 提供符号链接。将此目录添加到 `$PATH` 以自动使用 `ccache`。
> 更多信息：<https://ccache.dev/manual/latest.html>.

- 显示当前缓存统计信息：

`ccache {{[-s|--show-stats]}}`

- 清除所有缓存：

`ccache {{[-C|--clear]}}`

- 重置统计信息（但不清除缓存本身）：

`ccache {{[-z|--zero-stats]}}`

- 编译 C 代码并缓存编译输出（要对所有 `gcc` 调用使用 `ccache`，请参见上面的注意）：

`ccache gcc {{path/to/file.c}}`
