# clj

> Clojure tool to start a REPL or invoke a specific function with data.
> All options can be defined in a `deps.edn` file.
> More information: <https://clojure.org/guides/deps_and_cli>.

- Start a REPL:

`clj`

- Exec function:

`clojure -X {{namespace/fn_name}}`

- Run -main function of a namespace:

`clojure -M -m {{namespace}} {{args}}`

- Prepare (resolve deps, download libraries, make and cache classpaths):

`clojure -P`

- Start nREPL server with CIDER middleware:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}}}' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- Start REPL for ClojureScript and open browser:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}}}' --main cljs.main --repl`
