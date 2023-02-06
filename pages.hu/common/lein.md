# lein

> Clojure projektek kezelése deklaratív konfigurációval. További információ: <https://leiningen.org>.

- Egy új projekt állványzatának generálása egy sablon alapján:

`lein new {{template_name}} {{project_name}}`

- Indítson el egy REPL munkamenetet akár a projekttel együtt, akár önállóan:

`lein repl`

- A projekt `-main` függvényének futtatása opcionális argokkal:

`lein run {{args}}`

- A projekt tesztjeinek futtatása:

`lein test`

- Csomagolja a projektfájlokat és az összes függőséget egy jar fájlba:

`lein uberjar`
