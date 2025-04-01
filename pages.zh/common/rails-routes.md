# rails routes

> 列出 Rails 应用程序中的路由。
> 更多信息：<https://guides.rubyonrails.org/routing.html>.

- 列出所有路由：

`rails routes`

- 以扩展格式列出所有路由：

`rails routes --expanded`

- 列出部分匹配 URL 辅助方法名称、HTTP 动词或 URL 路径的路由：

`rails routes -g {{posts_path|GET|/posts}}`

- 列出映射到指定控制器的路由：

`rails routes -c {{posts|Posts|Blogs::PostsController}}`
