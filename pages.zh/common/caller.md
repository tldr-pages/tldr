# caller

> 打印函数调用上下文。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-caller>.

- 打印当前函数被调用的行号和文件名：

`caller`

- 打印当前函数被调用的行号、函数名和文件名：

`caller 0`

- 打印回溯 `n` 帧的函数调用的行号、函数名和文件名：

`caller {{n}}`