# zola

> 一个将所有功能集成在单个二进制文件中的静态网站生成器。
> 更多信息：<https://www.getzola.org/documentation/getting-started/cli-usage/>。

- 在给定目录下创建 Zola 使用的目录结构：

`zola init {{my_site}}`

- 在删除 `public` 目录后构建整个网站：

`zola build`

- 将整个网站构建到一个不同的目录：

`zola build --output-dir {{path/to/output_directory/}}`

- 使用本地服务器构建并提供网站（默认地址是 `127.0.0.1:1111`）：

`zola serve`

- 像构建命令一样构建所有页面，但不将任何结果写入磁盘：

`zola check`