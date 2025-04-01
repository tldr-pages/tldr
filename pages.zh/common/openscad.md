# openscad

> 用于创建实心 3D CAD 对象的软件。
> 更多信息：<https://openscad.org>.

- 打开一个文件：

`openscad {{path/to/button.scad}}`

- 将文件转换为 STL 格式：

`openscad -o {{path/to/button.stl}} {{path/to/button.scad}}`

- 使用特定颜色方案将文件渲染为 PNG：

`openscad -o {{path/to/button.png}} --colorscheme {{Sunset}} {{path/to/button.scad}}`
