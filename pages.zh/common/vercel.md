# vercel

> 部署和管理你的 Vercel 部署。
> 更多信息：<https://vercel.com/docs/cli>.

- 部署当前目录：

`vercel`

- 部署当前目录到生产环境：

`vercel --prod`

- 部署一个目录：

`vercel {{path/to/project}}`

- 初始化一个示例项目：

`vercel init`

- 使用环境变量部署：

`vercel --env {{ENV}}={{var}}`

- 使用环境变量构建：

`vercel --build-env {{ENV}}={{var}}`

- 设置默认区域以启用部署：

`vercel --regions {{region_id}}`

- 移除一个部署：

`vercel remove {{project_name}}`
