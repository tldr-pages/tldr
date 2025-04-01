# pbmtolj

> 将 PBM 文件转换为 HP LaserJet 文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtolj.html>。

- 将 PBM 文件转换为 HP LaserJet 文件：

`pbmtolj {{path/to/input.pbm}} > {{path/to/output.lj}}`

- 使用指定的方法压缩输出文件：

`pbmtolj -{{packbits|delta|compress}} {{path/to/input.pbm}} > {{path/to/output.lj}}`

- 指定所需的分辨率：

`pbmtolj -resolution {{75|100|150|300|600}} {{path/to/input.pbm}} > {{path/to/output.lj}}`
