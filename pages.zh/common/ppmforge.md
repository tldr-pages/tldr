# ppmforge

> 生成类似于云、行星和星空的分形图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmforge.html>。

- 生成行星图像：

`ppmforge > {{path/to/image.ppm}}`

- 生成云或夜空图像：

`ppmforge -{{night|clouds}} > {{path/to/image.ppm}}`

- 使用自定义网格大小和维度进行分形生成，并指定输出的尺寸：

`ppmforge -mesh {{512}} -dimension {{2.5}} -xsize {{1000}} -ysize {{1000}} > {{path/to/image.ppm}}`

- 控制生成的行星的倾斜角度和照明角度：

`ppmforge -tilt {{-15}} -hour {{12}} > {{path/to/image.ppm}}`