# turbo

> 高性能的构建系统，用于 JavaScript 和 TypeScript 代码库。
> 另见：`nx`。
> 更多信息：<https://turborepo.org/docs/reference/command-line-reference>。

- 使用默认网页浏览器和 Vercel 帐户登录：

`turbo login`

- 将当前目录链接到 Vercel 组织并启用远程缓存：

`turbo link`

- 构建当前项目：

`turbo run build`

- 在不并发的情况下运行任务：

`turbo run {{task_name}} --concurrency={{1}}`

- 运行任务时忽略缓存的工件，并强制重新执行所有任务：

`turbo run {{task_name}} --force`

- 在各个包之间并行运行任务：

`turbo run {{task_name}} --parallel --no-cache`

- 从 Vercel 组织中取消链接当前目录，并禁用远程缓存：

`turbo unlink`

- 生成特定任务执行的 Dot 图（输出文件格式可以通过文件名控制）：

`turbo run {{task_name}} --graph={{path/to/file.html|jpg|json|pdf|png|svg}}`