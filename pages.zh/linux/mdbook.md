# mdbook

> 通过编写 Markdown 文件创建在线书籍。
> 更多信息：<https://rust-lang.github.io/mdBook/>.

- 在当前目录中创建一个 mdbook 项目：

`mdbook init`

- 在特定目录中创建一个 mdbook 项目：

`mdbook init {{path/to/directory}}`

- 清理生成书籍的目录：

`mdbook clean`

- 在 <http://localhost:3000> 服务书籍，并在文件更改时自动构建：

`mdbook serve`

- 监视一组 Markdown 文件，并在文件更改时自动构建：

`mdbook watch`