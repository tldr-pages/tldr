# seq

> 打印数字序列到标准输出。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/seq-invocation.html>.

- 从 1 到 10 的序列：

`seq 10`

- 从 5 开始，3 为步长，不超过 20 的序列：

`seq 5 3 20`

- 从 5 开始，3 为步长，不超过 20 的序列，并用空格作为分隔符：

`seq {{[-s|--separator]}} " " 5 3 20`

- 从 5 开始，3 为步长，不超过 20 的序列，并格式化为 4 位宽度，不足 4 位，前面补 0：

`seq {{[-f|--format]}} "%04g" 5 3 20`
