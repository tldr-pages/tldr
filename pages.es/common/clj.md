# clj

> Herramienta de Clojure para usar una interfaz interactiva (REPL) o invocar una función con datos.
> Todas las opciones se pueden definir en un archivo `deps.edn`.
> Más información: <https://clojure.org/guides/deps_and_cli>.

- Inicia una REPL (interfaz interactiva):

`clj`

- Ejecuta una función:

`clj -X {{namespace/nombre_de_función}}`

- Ejecuta la función principal de un espacio de nombres (namespace) especificado:

`clj -M -m {{namespace}} {{argumentos}}`

- Prepara un proyecto resolviendo dependencias, descargando bibliotecas y haciendo/cacheando rutas de clases (classpaths):

`clj -P`

- Inicia un servidor nREPL con el software intermedio (middleware) CIDER:

`clj -Sdeps '{:deps {nrepl {:mvn/version "0.7.0"} cider/cider-nrepl {:mvn/version "0.25.2"}}}' -m nrepl.cmdline --middleware '["cider.nrepl/cider-middleware"]' --interactive`

- Inicia un REPL de ClojureScript y abre un navegador web:

`clj -Sdeps '{:deps {org.clojure/clojurescript {:mvn/version "1.10.758"}}}' --main cljs.main --repl`
