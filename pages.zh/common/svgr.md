# svgr

> 将 SVG 转换为 React 组件。
> 更多信息：<https://react-svgr.com>。

- 将 SVG 文件转换为 React 组件并输出到 `stdout`：

`svgr -- {{path/to/file.svg}}`

- 使用 TypeScript 将 SVG 文件转换为 React 组件并输出到 `stdout`：

`svgr --typescript -- {{path/to/file.svg}}`

- 使用 JSX 转换将 SVG 文件转换为 React 组件并输出到 `stdout`：

`svgr --jsx-runtime automatic -- {{path/to/file.svg}}`

- 将目录中的所有 SVG 文件转换为 React 组件并输出到指定目录：

`svgr --out-dir {{path/to/output_directory}} {{path/to/input_directory}}`

- 将目录中的所有 SVG 文件转换为 React 组件并输出到指定目录，跳过已转换的文件：

`svgr --out-dir {{path/to/output_directory}} --ignore-existing {{path/to/input_directory}}`

- 将目录中的所有 SVG 文件转换为 React 组件并输出到指定目录，指定文件名的命名方式：

`svgr --out-dir {{path/to/output_directory}} --filename-case {{camel|kebab|pascal}} {{path/to/input_directory}}`

- 将目录中的所有 SVG 文件转换为 React 组件并输出到指定目录，不生成索引文件：

`svgr --out-dir {{path/to/output_directory}} --no-index {{path/to/input_directory}}`