# shiori

> 用 Go 编写的简单书签管理器。
> 更多信息：<https://github.com/go-shiori/shiori>。

- 从 HTML Netscape 书签格式文件导入书签：

`shiori import {{path/to/bookmarks.html}}`

- 将指定的 URL 保存为书签：

`shiori add {{url}}`

- 列出已保存的书签：

`shiori print`

- 在浏览器中打开已保存的书签：

`shiori open {{bookmark_id}}`

- 在端口 8181 启动用于管理书签的 Web 界面：

`shiori serve --port {{8181}}`
