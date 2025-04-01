# osv-scanner

> 扫描各种媒介的依赖项，并将其与 OSV 数据库中的条目匹配。
> 更多信息：<https://osv.dev/about>.

- 扫描 Docker 镜像：

`osv-scanner -D {{docker_image_name}}`

- 扫描包锁定文件：

`osv-scanner -L {{path/to/lockfile}}`

- 扫描 SBOM 文件：

`osv-scanner -S {{path/to/sbom_file}}`

- 递归扫描多个目录：

`osv-scanner -r {{directory1 directory2 ...}}`

- 跳过扫描 Git 仓库：

`osv-scanner --skip-git {{-r|-D}} {{target}}`

- 以 JSON 格式输出结果：

`osv-scanner --json {{-D|-L|-S|-r}} {{target}}`
