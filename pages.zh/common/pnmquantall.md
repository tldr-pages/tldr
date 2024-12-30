# pnmquantall

> 在多个文件上同时运行 `pnmquant`，使它们共享一个公共的调色板。
> 另见：`pnmquant`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmquantall.html>。

- 使用指定的参数在多个文件上运行 `pnmquant`，覆盖原始文件：

`pnmquantall {{n_colors}} {{path/to/input1.pnm path/to/input2.pnm ...}}`

- 将量化后的图像保存为与输入文件同名但附加指定扩展名的文件：

`pnmquantall -ext {{extension}} {{n_colors}} {{path/to/input1.pnm path/to/input2.pnm ...}}`