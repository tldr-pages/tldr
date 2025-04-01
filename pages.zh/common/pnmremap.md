# pnmremap

> 替换 PNM 图像中的颜色。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmremap.html>.

- 用指定的颜色调色板替换图像中的颜色：

`pnmremap -mapfile {{path/to/palette_file.ppm}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 使用 Floyd-Steinberg 阈值处理来表示调色板中缺失的颜色：

`pnmremap -mapfile {{path/to/palette_file.ppm}} -floyd {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 使用调色板中的第一个颜色来表示调色板中缺失的颜色：

`pnmremap -mapfile {{path/to/palette_file.ppm}} -firstisdefault {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- 使用指定的颜色来表示调色板中缺失的颜色：

`pnmremap -mapfile {{path/to/palette_file.ppm}} -missingcolor {{color}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
