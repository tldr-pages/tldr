# bun exec

> Esegui comandi shell o file di script usando il runtime di Bun.
> Nota: quando esegui dalla shell, ricorda di sfuggire alle virgolette.
> Maggiori informazioni: <https://bun.com/docs/runtime/shell>.

- Esegui un comando semplice:

`bun exec "echo hello"`

- Esegui un comando con flag:

`bun exec "ls -la"`

- Esegui un comando contenente virgolette:

`bun exec "echo \"hello friends\""`

- Esegui un comando shell combinato:

`bun exec "mkdir test && cd test"`

- Esegui un file di script:

`bun exec {{percorso/dello/script}}`
