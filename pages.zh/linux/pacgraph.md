# pacgraph

> 绘制已安装软件包的图形并导出为 PNG/SVG/GUI/控制台。
> 更多信息：<https://github.com/keenerd/pacgraph>。

- 生成 SVG 和 PNG 图形：

`pacgraph`

- 生成 SVG 图形：

`pacgraph --svg`

- 将摘要打印到控制台：

`pacgraph --console`

- 覆盖默认的文件名/位置（注意：请勿指定文件扩展名）：

`pacgraph --file={{path/to/file}}`

- 更改非依赖软件包的颜色：

`pacgraph --top={{color}}`

- 更改软件包依赖的颜色：

`pacgraph --dep={{color}}`

- 更改图形的背景颜色：

`pacgraph --background={{color}}`

- 更改软件包之间链接的颜色：

`pacgraph --link={{color}}`