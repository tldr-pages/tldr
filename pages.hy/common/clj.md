# clj

> Clojure գործիք՝ REPL սկսելու կամ տվյալների հետ ֆունկցիա կանչելու համար:.
> Բոլոր տարբերակները կարող են սահմանվել `deps.edn` ֆայլում:.
> Լրացուցիչ տեղեկություններ. <https://clojure.org/guides/deps_and_cli>:.

- Սկսեք REPL (ինտերակտիվ կեղև).:

`clj`

- Կատարել գործառույթ.:

`clj -X {{namespace/function_name}}`

- Գործարկեք նշված անվանատարածքի հիմնական գործառույթը.:

`clj -M {{[-m|--main]}} {{namespace}} {{args}}`

- Պատրաստեք նախագիծ՝ լուծելով կախվածությունները, ներբեռնելով գրադարանները և ստեղծելով/քեշավորելով դասուղիները.:

`clj -P`

- Սկսեք nREPL սերվերը CIDER միջին ծրագրով.:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}}}' {{[-m|--main]}} nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- Սկսեք REPL ClojureScript-ի համար և բացեք վեբ զննարկիչ.:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}}}' {{[-m|--main]}} cljs.main {{[-r|--repl]}}`
