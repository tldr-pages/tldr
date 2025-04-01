# pnmquantall

> 对多个文件同时运行 `pnmquant`，使它们共享一个通用的调色板。
> 参见：`pnmquant`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmquantall.html>。

- 使用指定参数对多个文件运行 `pnmquant`，覆盖原始文件：

`pnmquantall {{n_colors}} {{path/to/input1.pnm path/to/input2.pnm ...}}`

- 将量化后的图像保存到与输入文件同名的文件中，但附加指定的扩展名：

`pnmquantall -ext {{extension}} {{n_colors}} {{path/to/input1.pnm path/to/input2.pnm ...}}`
