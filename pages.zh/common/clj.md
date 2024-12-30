# clj

> Clojure 工具，用于启动 REPL 或使用数据调用函数。
> 所有选项可以在 `deps.edn` 文件中定义。
> 更多信息：<https://clojure.org/guides/deps_and_cli>。

- 启动 REPL（交互式 shell）：

`clj`

- 执行一个函数：

`clj -X {{namespace/function_name}}`

- 运行指定命名空间的主函数：

`clj -M -m {{namespace}} {{args}}`

- 准备一个项目，通过解析依赖关系、下载库以及创建/缓存类路径：

`clj -P`

- 启动一个带有 CIDER 中间件的 nREPL 服务器：

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}}}' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- 启动一个 ClojureScript 的 REPL 并打开一个网页浏览器：

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}}}' --main cljs.main --repl`