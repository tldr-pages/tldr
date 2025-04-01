# xxhsum

> 使用快速的非加密算法 xxHash 打印或验证校验和。
> 更多信息：<https://github.com/Cyan4973/xxHash>。

- 使用特定算法计算文件的校验和：

`xxhsum -H{{0|32|64|128}} {{path/to/file}}`

- 运行基准测试：

`xxhsum -b`