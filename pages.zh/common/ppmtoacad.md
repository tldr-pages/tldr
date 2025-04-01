# ppmtoacad

> 将 PPM 图像转换为 AutoCAD 数据库或幻灯片。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmtoacad.html>.

- 将 PPM 图像转换为 AutoCAD 幻灯片：

`ppmtoacad {{path/to/file.ppm}} > {{path/to/file.acad}}`

- 将 PPM 图像转换为 AutoCAD 二进制数据库导入文件：

`ppmtoacad -dxb {{path/to/file.ppm}} > {{path/to/file.dxb}}`

- 限制输出中的颜色为 8 种 RGB 阴影：

`ppmtoacad -8 {{path/to/file.ppm}} > {{path/to/file.dxb}}`