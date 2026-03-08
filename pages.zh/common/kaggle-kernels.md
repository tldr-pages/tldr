# kaggle kernels

> 管理 Kaggle 内核（即代码/笔记本）。
> 更多信息：<https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#kernels>。

- 列出所有内核：

`kaggle {{[k|kernels]}} list`

- 列出指定内核的输出文件：

`kaggle {{[k|kernels]}} files {{内核名称}}`

- 为内核初始化元数据文件（默认为当前目录）：

`kaggle {{[k|kernels]}} init {{[-p|--path]}} {{目录路径}}`

- 将新代码推送（push）到内核并运行：

`kaggle {{[k|kernels]}} push {{[-p|--path]}} {{目录路径}}`

- 拉取（pull）指定的内核到本地：

`kaggle {{[k|kernels]}} pull {{内核名称}} {{[-p|--path]}} {{目录路径}}`

- 获取最近一次内核运行的输出数据：

`kaggle {{[k|kernels]}} output {{内核名称}}`

- 显示最近一次内核运行的状态：

`kaggle {{[k|kernels]}} status {{内核名称}}`
