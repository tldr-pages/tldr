# boot

> Strumenti di build per il linguaggio di programmazione Clojure.
> Maggiori informazioni: <https://github.com/boot-clj/boot>.

- Avvia una sessione REPL con il progetto o da sola:

`boot repl`

- Builda un singolo `uberjar`:

`boot jar`

- Mostra aiuto per un comando:

`boot cljs --help`

- Genera le fondamenta per un nuovo progetto basandoti su una template:

`boot --dependencies boot/new new --template {{nome_template}} --name {{nome_progetto}}`

- Builda per development (se si sta utilizzando il template boot/new):

`boot dev`

- BUilda per produzione (se si sta utilizzando il template boot/new):

`boot prod`
