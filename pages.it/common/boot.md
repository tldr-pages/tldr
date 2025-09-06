# boot

> Strumenti di implementazione per il linguaggio di programmazione Clojure.
> Maggiori informazioni: <https://github.com/boot-clj/boot>.

- Avvia una sessione REPL con il progetto o autonomamente (standalone):

`boot repl`

- Implementa un singolo `uberjar`:

`boot jar`

- Genera lo scheletro di un nuovo progetto basato su un modello di codice esistente:

`boot --dependencies boot/new new --template {{nome_del_modello}} --name {{nome_del_progetto}}`

- Implementa l'ambiente di sviluppo (se si sta utilizzando il modello di codice boot/new):

`boot dev`

- Implementa l'ambiente di produzione (se si sta utilizzando il modello di codice boot/new):

`boot prod`

- Mostra la descrizione di uno specifico comando:

`boot {{task}} --help`
