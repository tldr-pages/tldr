# zola

> 一个静态站点生成器，一个二进制文件内包含所有功能。
> 更多信息：<https://www.getzola.org/documentation/getting-started/cli-usage/>.

- 在指定目录下创建 Zola 使用的目录结构：

`zola init {{我的站点}}`

- 在删除 `public` 目录后构建整个站点：

`zola build`

- 将整个站点构建到另一个目录中：

`zola build --output-dir {{路径/到/输出_目录/}}`

- 使用本地服务器构建并服务站点（默认是 `127.0.0.1:1111`）：

`zola serve`

- 构建所有页面，就像构建命令一样，但不将结果写入磁盘：

`zola check`
