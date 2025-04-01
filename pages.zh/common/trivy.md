# trivy

> 用于扫描容器镜像、文件系统和 Git 仓库中的漏洞，以及配置问题的扫描器。
> 更多信息：<https://aquasecurity.github.io/trivy>.

- 扫描 Docker 镜像以查找漏洞和暴露的秘密：

`trivy image {{image:tag}}`

- 扫描 Docker 镜像并按严重性过滤输出：

`trivy image --severity {{HIGH,CRITICAL}} {{alpine:3.15}}`

- 扫描 Docker 镜像，忽略任何未修复/未打补丁的漏洞：

`trivy image --ignore-unfixed {{alpine:3.15}}`

- 扫描文件系统以查找漏洞和配置错误：

`trivy fs --security-checks {{vuln,config}} {{path/to/project_directory}}`

- 扫描 IaC（Terraform、CloudFormation、ARM、Helm 和 Dockerfile）目录以查找配置错误：

`trivy config {{path/to/iac_directory}}`

- 扫描本地或远程 Git 仓库以查找漏洞：

`trivy repo {{path/to/local_repository_directory|remote_repository_URL}}`

- 扫描 Git 仓库直到特定的提交哈希：

`trivy repo --commit {{commit_hash}} {{repository}}`

- 使用 SARIF 模板生成输出：

`trivy image --format {{template}} --template "{{@sarif.tpl}}" -o {{path/to/report.sarif}} {{image:tag}}`