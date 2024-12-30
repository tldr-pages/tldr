# webpack

> 将一个网页项目的 js 文件和其他资源打包成一个单一的输出文件。
> 更多信息：<https://webpack.js.org>。

- 从入口文件创建单一输出文件：

`webpack {{app.js}} {{bundle.js}}`

- 从 JavaScript 文件中加载 CSS 文件（这使用 CSS 加载器处理 CSS 文件）：

`webpack {{app.js}} {{bundle.js}} --module-bind '{{css=css}}'`

- 传递一个配置文件（例如入口脚本和输出文件名）并显示编译进度：

`webpack --config {{webpack.config.js}} --progress`

- 在项目文件更改时自动重新编译：

`webpack --watch {{app.js}} {{bundle.js}}`