# boot

> Construiți instrumente pentru limbajul de programare Clojure.
> Mai multe informaţii: <https://github.com/boot-clj/boot>

- Începeți o sesiune REPL fie cu proiectul, fie independent:

`boot repl`

- Construiți un singur `uberjar`:

`boot jar`

- Aflați mai multe despre o comandă:

`boot cljs --help`

- Generarea schelei pentru un nou proiect bazat pe un șablon:

`boot --dependencies boot/new new --template {{template_name}} --name {{project_name}}`

- Construiți pentru dezvoltare (dacă utilizați șablonul boot/nou):

`boot dev`

- Construiți pentru producție (dacă utilizați cizme/șablon nou):

`boot prod`
