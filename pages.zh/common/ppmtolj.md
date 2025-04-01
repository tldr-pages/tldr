# ppmtolj

> 将 PPM 文件转换为 HP LaserJet PCL 5 彩色文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtolj.html>.

- 将 PPM 文件转换为 HP LaserJet PCL 5 彩色文件：

`ppmtolj {{path/to/input.ppm}} > {{path/to/output.lj}}`

- 使用指定的伽玛值进行伽玛校正：

`ppmtolj -gamma {{gamma}} {{path/to/input.ppm}} > {{path/to/output.lj}}`

- 指定所需的分辨率：

`ppmtolj -resolution {{75|100|150|300|600}} {{path/to/input.ppm}} > {{path/to/output.lj}}`