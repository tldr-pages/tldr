# clj

> Clojure tool om een REPL te starten of roep een een specifieke functie aan met data.
> Alle opties kunnen worden gedefinieerd in een `deps.edn` bestand.
> Meer informatie: <https://clojure.org/guides/deps_and_cli>.

- Start een REPL (interactieve shell):

`clj`

- Voer een functie uit:

`clj -X {{namespace/functie_naam}}`

- Voer de voornaamste functie uit van een gespecificeerde namespace:

`clj -M -m {{namespace}} {{args}}`

- Bereid een project voor door afhankelijkheden op te lossen, het downloaden van bibliotheken en het maken/cachen van classpaths:

`clj -P`

- Start een nREPL server met de CIDER middleware:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}}}' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- Start een REPL voor ClojureScript en open een web browser:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}}}' --main cljs.main --repl`
