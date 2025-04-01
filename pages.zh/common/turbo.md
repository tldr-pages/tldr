# turbo

> 高性能的 JavaScript 和 TypeScript 代码库构建系统。
> 参见: `nx`。
> 更多信息: <https://turborepo.org/docs/reference/command-line-reference>。

- 使用默认的网页浏览器和 Vercel 账户登录:

`turbo login`

- 将当前目录链接到 Vercel 组织并启用远程缓存:

`turbo link`

- 构建当前项目:

`turbo run build`

- 无并发地运行一个任务:

`turbo run {{task_name}} --concurrency={{1}}`

- 忽略缓存的工件并强制重新执行所有任务:

`turbo run {{task_name}} --force`

- 在包之间并行运行一个任务:

`turbo run {{task_name}} --parallel --no-cache`

- 解除当前目录与 Vercel 组织的链接并禁用远程缓存:

`turbo unlink`

- 生成特定任务执行的 Dot 图形（输出文件格式可以通过文件名控制）:

`turbo run {{task_name}} --graph={{path/to/file.html|jpg|json|pdf|png|svg}}`
