# quarto

> 一个基于 Pandoc 的开源科学和技术出版系统。
> 更多信息：<https://quarto.org/>.

- 创建一个新项目：

`quarto create-project {{路径/到/目录}} --type {{book|default|website}}`

- 创建一个新的博客网站：

`quarto create-project {{路径/到/目录}} --type {{website}} --template {{blog}}`

- 将输入文件渲染为不同格式：

`quarto render {{路径/到/文件.[qmd|rmd|ipynb]}} --to {{html|pdf|docx}}`

- 渲染并预览文档或网站：

`quarto preview {{路径/到/目录 | 路径/到/文件}}`

- 发布文档或项目到 Quarto Pub、Github Pages、RStudio Connect 或 Netlify：

`quarto publish {{quarto-pub|gh-pages|connect|netlify}}`
