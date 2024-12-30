# seq

> 输出一系列数字到 `stdout`。
> 更多信息：<https://www.gnu.org/software/coreutils/seq>。

- 从 1 到 10 的序列：

`seq 10`

- 从 5 到 20 的每第 3 个数字：

`seq 5 3 20`

- 用空格而不是换行符分隔输出：

`seq -s " " 5 3 20`

- 格式化输出宽度，最小为 4 位，必要时用零填充：

`seq -f "%04g" 5 3 20`