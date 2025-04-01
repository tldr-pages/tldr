# gitleaks

> 检测 Git 仓库中泄露的秘密和 API 密钥。
> 更多信息：<https://github.com/gitleaks/gitleaks>.

- 扫描远程仓库：

`gitleaks detect --repo-url {{https://github.com/username/repository.git}}`

- 扫描本地目录：

`gitleaks detect --source {{path/to/repository}}`

- 将扫描结果输出到 JSON 文件：

`gitleaks detect --source {{path/to/repository}} --report {{path/to/report.json}}`

- 使用自定义规则文件：

`gitleaks detect --source {{path/to/repository}} --config-path {{path/to/config.toml}}`

- 从特定的提交开始扫描：

`gitleaks detect --source {{path/to/repository}} --log-opts {{--since=commit_id}}`

- 在提交前扫描未提交的更改：

`gitleaks protect --staged`

- 显示详细的输出，显示在扫描中哪些部分被识别为泄露：

`gitleaks protect --staged --verbose`