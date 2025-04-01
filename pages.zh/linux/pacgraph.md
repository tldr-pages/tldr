# pacgraph

> 绘制安装包的 PNG/SVG/图形界面/控制台图形。
> 更多信息：<https://github.com/keenerd/pacgraph>。

- 生成 SVG 和 PNG 图形：

`pacgraph`

- 生成 SVG 图形：

`pacgraph --svg`

- 在控制台打印摘要：

`pacgraph --console`

- 覆盖默认的文件名/位置（注意：不要指定文件扩展名）：

`pacgraph --file={{path/to/file}}`

- 更改非依赖包的颜色：

`pacgraph --top={{color}}`

- 更改包依赖的颜色：

`pacgraph --dep={{color}}`

- 更改图形的背景颜色：

`pacgraph --background={{color}}`

- 更改包之间链接的颜色：

`pacgraph --link={{color}}`
