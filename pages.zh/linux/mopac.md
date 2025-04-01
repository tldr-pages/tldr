# mopac

> MOPAC（分子轨道套件）是一个基于 Dewar 和 Thiel 的 NDDO 近似的半经验量子化学程序。
> 更多信息：<https://github.com/openmopac/mopac>。

- 根据输入文件（`.mop`、`.dat` 和 `.arc`）执行计算：

`mopac {{path/to/input_file}}`

- 最小工作示例，使用 HF 方法，将输出写入当前目录并实时显示输出文件：

`touch test.out; echo "PM7\n#comment\n\nH 0.95506 0.05781 -0.03133\nF 1.89426 0.05781 -0.03133" > test.mop; mopac test.mop & tail -f test.out`