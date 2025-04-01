# ldd

> 显示二进制文件的共享库依赖。
> 不要在不受信任的二进制文件上使用此命令，应使用 objdump。
> 更多信息：<https://manned.org/ldd>.

- 显示二进制文件的共享库依赖：

`ldd {{path/to/binary}}`

- 显示依赖的所有信息：

`ldd --verbose {{path/to/binary}}`

- 显示未使用的直接依赖：

`ldd --unused {{path/to/binary}}`

- 报告缺失的数据对象并执行数据重定位：

`ldd --data-relocs {{path/to/binary}}`

- 报告缺失的数据对象和函数，并执行数据和函数的重定位：

`ldd --function-relocs {{path/to/binary}}`
