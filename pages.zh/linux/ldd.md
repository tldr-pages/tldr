# ldd

> 显示二进制文件的共享库依赖关系。
> 不要在不可信的二进制文件上使用，建议使用 objdump。
> 更多信息：<https://manned.org/ldd>。

- 显示二进制文件的共享库依赖关系：

`ldd {{path/to/binary}}`

- 显示关于依赖关系的所有信息：

`ldd --verbose {{path/to/binary}}`

- 显示未使用的直接依赖关系：

`ldd --unused {{path/to/binary}}`

- 报告缺失的数据对象并执行数据重定位：

`ldd --data-relocs {{path/to/binary}}`

- 报告缺失的数据对象和函数，并为两者执行重定位：

`ldd --function-relocs {{path/to/binary}}`