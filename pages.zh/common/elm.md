# elm

> 编译和运行 Elm 源文件。
> 更多信息：<https://elm-lang.org>。

- 初始化一个 Elm 项目，生成一个 `elm.json` 文件：

`elm init`

- 启动交互式的 Elm shell：

`elm repl`

- 编译一个 Elm 文件，将结果输出到 `index.html` 文件：

`elm make {{source}}`

- 编译一个 Elm 文件，将结果输出到一个 JavaScript 文件：

`elm make {{source}} --output={{destination}}.js`

- 启动一个本地 Web 服务器，在页面加载时编译 Elm 文件：

`elm reactor`

- 从 <https://package.elm-lang.org> 安装 Elm 包：

`elm install {{author}}/{{package}}`