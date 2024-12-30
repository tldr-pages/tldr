# satis

> Satis 静态 Composer 仓库的命令行工具。
> 更多信息：<https://github.com/composer/satis>。

- 初始化 Satis 配置：

`satis init {{satis.json}}`

- 将 VCS 仓库添加到 Satis 配置中：

`satis add {{repository_url}}`

- 从配置中构建静态输出：

`satis build {{satis.json}} {{path/to/output_directory}}`

- 通过仅更新指定的仓库来构建静态输出：

`satis build --repository-url {{repository_url}} {{satis.json}} {{path/to/output_directory}}`

- 删除无用的归档文件：

`satis purge {{satis.json}} {{path/to/output_directory}}`