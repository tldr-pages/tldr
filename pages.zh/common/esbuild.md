# esbuild

> 为速度而构建的 JavaScript 打包器和压缩器。
> 更多信息：<https://esbuild.github.io/>.

- 打包一个 JavaScript 应用并输出到 `stdout`：

`esbuild --bundle {{path/to/file.js}}`

- 从 `stdin` 打包一个 JSX 应用：

`esbuild --bundle --outfile={{path/to/out.js}} < {{path/to/file.jsx}}`

- 在 `生产` 模式下打包并压缩一个带源映射的 JSX 应用：

`esbuild --bundle --define:{{process.env.NODE_ENV=\"production\"}} --minify --sourcemap {{path/to/file.js}}`

- 针对一组用逗号分隔的浏览器打包一个 JSX 应用：

`esbuild --bundle --minify --sourcemap --target={{chrome58,firefox57,safari11,edge16}} {{path/to/file.jsx}}`

- 针对特定的节点版本打包一个 JavaScript 应用：

`esbuild --bundle --platform={{node}} --target={{node12}} {{path/to/file.js}}`

- 在 `.js` 文件中启用 JSX 语法来打包一个 JavaScript 应用：

`esbuild --bundle app.js --loader:{{.js=jsx}} {{path/to/file.js}}`

- 打包并在 HTTP 服务器上提供一个 JavaScript 应用：

`esbuild --bundle --serve={{port}} --outfile={{index.js}} {{path/to/file.js}}`

- 将文件列表打包到输出目录：

`esbuild --bundle --outdir={{path/to/output_directory}} {{path/to/file1 path/to/file2 ...}}`