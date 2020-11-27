# clj

> Clojure tool to start a REPL or invoke a specific function with data.
> All options can be defined in a `deps.edn` file.
> More information: <https://clojure.org/guides/deps_and_cli>.

- Start a REPL:

`clj`

- Exec function:

`clojure [clj-opt*] -X[:aliases] [a/fn] [kpath v]*`

- Run main:

`clojure [clj-opt*] -M[:aliases] [init-opt*] [main-opt] [arg*]`

- Prepare:

`clojure [clj-opt*] -P [other exec opts]`

- Start nREPL server with CIDER middleware:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}}}' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- Start REPL for ClojureScript and open browser:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}}}' --main cljs.main --repl`
