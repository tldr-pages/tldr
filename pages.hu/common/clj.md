# clj

> Clojure eszköz egy REPL indítására vagy egy adott függvény meghívására adatokkal. Minden opciót a `deps.edn` fájlban lehet definiálni. További információ: <https://clojure.org/guides/deps_and_cli>.

- REPL indítása (interaktív héj):

`clj`

- Egy függvény végrehajtása:

`clj -X {{namespace/function_name}}`

- Egy megadott névtér főfüggvényének futtatása:

`clj -M -m {{namespace}} {{args}}`

- Egy projekt előkészítése a függőségek feloldásával, könyvtárak letöltésével és osztályútvonalak készítésével / gyorsítótárazásával:

`clj -P`

- Egy nREPL-kiszolgáló indítása a CIDER middleware segítségével:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}}}' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- Indítson el egy REPL-t a ClojureScript számára, és nyisson meg egy webböngészőt:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}}}' --main cljs.main --repl`
