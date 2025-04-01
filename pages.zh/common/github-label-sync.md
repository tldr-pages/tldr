# github-label-sync

> 同步 GitHub 标签。
> 更多信息：<https://github.com/Financial-Times/github-label-sync>.

- 使用本地 `labels.json` 文件同步标签：

`github-label-sync --access-token {{token}} {{repository_name}}`

- 使用特定的标签 JSON 文件同步标签：

`github-label-sync --access-token {{token}} --labels {{url|path/to/json_file}} {{repository_name}}`

- 执行预演操作，而不实际同步标签：

`github-label-sync --access-token {{token}} --dry-run {{repository_name}}`

- 保留不在 `labels.json` 中的标签：

`github-label-sync --access-token {{token}} --allow-added-labels {{repository_name}}`

- 使用 `GITHUB_ACCESS_TOKEN` 环境变量同步：

`github-label-sync {{repository_name}}`
