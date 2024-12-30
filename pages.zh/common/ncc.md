# ncc

> 将 Node.js 应用程序编译成单个文件。
> 支持 TypeScript、二进制插件和动态引用。
> 更多信息：<https://github.com/vercel/ncc>。

- 打包 Node.js 应用程序：

`ncc build {{path/to/file.js}}`

- 打包并压缩 Node.js 应用程序：

`ncc build --minify {{path/to/file.js}}`

- 打包、压缩 Node.js 应用程序并生成源映射：

`ncc build --source-map {{path/to/file.js}}`

- 在源文件更改时自动重新编译：

`ncc build --watch {{path/to/file.js}}`

- 将 Node.js 应用程序打包到临时目录并运行以进行测试：

`ncc run {{path/to/file.js}}`

- 清理 `ncc` 缓存：

`ncc clean cache`