# ppmtolj

> 将PPM文件转换为HP LaserJet PCL 5彩色文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtolj.html>。

- 将PPM文件转换为HP LaserJet PCL 5彩色文件：

`ppmtolj {{path/to/input.ppm}} > {{path/to/output.lj}}`

- 使用指定的伽玛值应用伽玛校正：

`ppmtolj -gamma {{gamma}} {{path/to/input.ppm}} > {{path/to/output.lj}}`

- 指定所需的分辨率：

`ppmtolj -resolution {{75|100|150|300|600}} {{path/to/input.ppm}} > {{path/to/output.lj}}`