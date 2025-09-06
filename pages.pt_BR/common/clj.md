# clj

> Ferramenta de Clojure para iniciar um REPL ou invocar uma função com argumentos.
> Todas as opções podem ser definidas em um arquivo `deps.edn`.
> Mais informações: <https://clojure.org/guides/deps_and_cli>.

- Inicia um REPL:

`clj`

- Executa uma função:

`clj -X {{namespace/function_name}}`

- Executa a função principal (main) do namespace especificado:

`clj -M -m {{namespace}} {{args}}`

- Prepara um projeto resolvendo dependências, baixando bibliotecas, e criando / cacheando classpaths:

`clj -P`

- Inicia um servidor nREPL com o middleware CIDER:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}}}' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- Inicia um REPL para ClojureScript e abre um navegador web:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}}}' --main cljs.main --repl`
