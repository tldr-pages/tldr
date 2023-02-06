# boot

> Eszközök készítése a Clojure programozási nyelvhez. További információ: <https://github.com/boot-clj/boot>.

- Indítson el egy REPL munkamenetet a projekttel együtt vagy önállóan:

`boot repl`

- Építsen egyetlen `uberjar`:

`boot jar`

- Ismerjen meg egy parancsot:

`boot cljs --help`

- Állványzat generálása egy új projekthez egy sablon alapján:

`boot --dependencies boot/new new --template {{template_name}} --name {{project_name}}`

- Építés a fejlesztéshez (ha a boot/new sablont használja):

`boot dev`

- Build for production (ha a boot/new sablont használja):

`boot prod`
