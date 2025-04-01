# esbuild

> 为速度而设计的 JavaScript 打包器和压缩器。
> 更多信息：<https://esbuild.github.io/>.

- 打包 JavaScript 应用程序并输出到 `stdout`：

`esbuild --bundle {{path/to/file.js}}`

- 从 `stdin` 打包 JSX 应用程序：

`esbuild --bundle --outfile={{path/to/out.js}} < {{path/to/file.jsx}}`

- 以 `production` 模式启用源映射并打包和压缩 JSX 应用程序：

`esbuild --bundle --define:{{process.env.NODE_ENV=\"production\"}} --minify --sourcemap {{path/to/file.js}}`

- 为逗号分隔的浏览器列表打包和压缩 JSX 应用程序：

`esbuild --bundle --minify --sourcemap --target={{chrome58,firefox57,safari11,edge16}} {{path/to/file.jsx}}`

- 为特定的 Node.js 版本打包 JavaScript 应用程序：

`esbuild --bundle --platform={{node}} --target={{node12}} {{path/to/file.js}}`

- 打包 JavaScript 应用程序并启用 `.js` 文件中的 JSX 语法：

`esbuild --bundle app.js --loader:{{.js=jsx}} {{path/to/file.js}}`

- 打包并使用 HTTP 服务器提供 JavaScript 应用程序：

`esbuild --bundle --serve={{port}} --outfile={{index.js}} {{path/to/file.js}}`

- 将文件列表打包到输出目录：

`esbuild --bundle --outdir={{path/to/output_directory}} {{path/to/file1 path/to/file2 ...}}`