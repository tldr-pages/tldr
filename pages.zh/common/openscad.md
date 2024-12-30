# openscad

> 用于创建实心3D CAD对象的软件。
> 更多信息：<https://openscad.org>。

- 打开文件：

`openscad {{path/to/button.scad}}`

- 将文件转换为STL格式：

`openscad -o {{path/to/button.stl}} {{path/to/button.scad}}`

- 将文件渲染为特定颜色方案的PNG格式：

`openscad -o {{path/to/button.png}} --colorscheme {{Sunset}} {{path/to/button.scad}}`