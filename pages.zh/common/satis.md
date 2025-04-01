# satis

> Satis 静态 Composer 仓库的命令行工具。
> 更多信息：<https://github.com/composer/satis>。

- 初始化 Satis 配置：

`satis init {{satis.json}}`

- 向 Satis 配置中添加 VCS 仓库：

`satis add {{repository_url}}`

- 从配置构建静态输出：

`satis build {{satis.json}} {{path/to/output_directory}}`

- 仅更新指定仓库以构建静态输出：

`satis build --repository-url {{repository_url}} {{satis.json}} {{path/to/output_directory}}`

- 移除无用的存档文件：

`satis purge {{satis.json}} {{path/to/output_directory}}`