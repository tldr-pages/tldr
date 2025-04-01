# webpack

> 将一个 Web 项目的 JavaScript 文件和其他资源打包成一个输出文件。
> 更多信息：<https://webpack.js.org>.

- 从一个入口文件创建一个输出文件：

`webpack {{app.js}} {{bundle.js}}`

- 从 JavaScript 文件中加载 CSS 文件（这使用了 CSS 加载器来处理 CSS 文件）：

`webpack {{app.js}} {{bundle.js}} --module-bind '{{css=css}}'`

- 传递一个配置文件（例如，入口脚本和输出文件名）并显示编译进度：

`webpack --config {{webpack.config.js}} --progress`

- 当项目文件更改时自动重新编译：

`webpack --watch {{app.js}} {{bundle.js}}`