# clj

> Instrumentul Clojure pentru a porni un REPL sau pentru a invoca o anumită funcție cu date.
> Toate opțiunile pot fi definite într-un fișier `deps.edn”.
> Mai multe informaţii: <https://clojure.org/guides/deps_and_cli>

- Începe un REPL:

`clj`

- Execută o funcție:

`clj -X {{namespace/function_name}}`

- Rulați funcția principală a unui spațiu de nume specificat:

`clj -M -m {{namespace}} {{args}}`

- Pregătiți un proiect prin rezolvarea dependențelor, descărcarea bibliotecilor și crearea de clasificări în cache:

`clj -P`

- Porniți un server nrepl cu middleware CIDER:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}}}' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- Porniți un REPL pentru ClojureScript și deschideți un browser web:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}}}' --main cljs.main --repl`
