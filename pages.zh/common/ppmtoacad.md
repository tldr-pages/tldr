# ppmtoacad

> 将PPM图像转换为AutoCAD数据库或幻灯片。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtoacad.html>。

- 将PPM图像转换为AutoCAD幻灯片：

`ppmtoacad {{path/to/file.ppm}} > {{path/to/file.acad}}`

- 将PPM图像转换为AutoCAD二进制数据库导入文件：

`ppmtoacad -dxb {{path/to/file.ppm}} > {{path/to/file.dxb}}`

- 将输出中的颜色限制为8种RGB色调：

`ppmtoacad -8 {{path/to/file.ppm}} > {{path/to/file.dxb}}`