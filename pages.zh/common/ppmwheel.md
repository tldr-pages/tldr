# ppmwheel

> 生成一个颜色轮的PPM图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/ppmwheel.html>。

- 生成类型为 `Ppmcirc` 的颜色轮：

`ppmwheel {{直径}} > {{输出文件路径/output.ppm}}`

- 生成类型为 `Hue-value` 的颜色轮：

`ppmwheel -huevalue {{直径}} > {{输出文件路径/output.ppm}}`

- 生成类型为 `Hue-saturation` 的颜色轮：

`ppmwheel -huesaturation {{直径}} > {{输出文件路径/output.ppm}}`