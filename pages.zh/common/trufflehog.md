# trufflehog

> 在文件、Git 仓库、S3 存储桶和 Docker 镜像中查找和验证凭据。
> 更多信息：<https://github.com/trufflesecurity/trufflehog>.

- 扫描 Git 仓库以查找已验证的秘密：

`trufflehog git {{https://github.com/trufflesecurity/test_keys}} --only-verified`

- 扫描 GitHub 组织以查找已验证的秘密：

`trufflehog github --org={{trufflesecurity}} --only-verified`

- 扫描 GitHub 仓库以查找已验证的密钥并获取 JSON 输出：

`trufflehog git {{https://github.com/trufflesecurity/test_keys}} --only-verified --json`

- 扫描 GitHub 仓库及其 Issues 和 Pull Requests：

`trufflehog github --repo={{https://github.com/trufflesecurity/test_keys}} --issue-comments --pr-comments`

- 扫描 S3 存储桶以查找已验证的密钥：

`trufflehog s3 --bucket={{bucket name}} --only-verified`

- 使用 IAM 角色扫描 S3 存储桶：

`trufflehog s3 --role-arn={{iam-role-arn}}`

- 扫描单个文件或目录：

`trufflehog filesystem {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 扫描 Docker 镜像以查找已验证的秘密：

`trufflehog docker --image {{trufflesecurity/secrets}} --only-verified`