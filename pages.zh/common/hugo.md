# hugo

> 基于模板的静态网站生成器。使用模块、组件和主题。
> 一些子命令（如 `server`）有自己的使用文档。
> 更多信息：<https://gohugo.io>.

- 创建一个新的 Hugo 网站：

`hugo new site {{path/to/site}}`

- 创建一个新的 Hugo 主题（主题也可以从 <https://themes.gohugo.io/> 下载）：

`hugo new theme {{theme_name}}`

- 创建一个新页面：

`hugo new {{section_name}}/{{page_name}}`

- 将站点构建到 `./public/` 目录：

`hugo`

- 构建包含标记为“草稿”的页面的站点：

`hugo --buildDrafts`

- 在本地 IP 上构建站点：

`hugo server --bind {{local-ip}} --baseURL {{http://local-ip}}`

- 将站点构建到指定目录：

`hugo --destination {{path/to/destination}}`

- 构建站点，启动 web 服务器来提供服务，并在编辑页面时自动重新加载：

`hugo server`