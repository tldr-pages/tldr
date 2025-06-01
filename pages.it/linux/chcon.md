# chcon

> Cambia contesto di sicurezza SELinux di file o directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/chcon-invocation.html>.

- Mostra il contesto di sicurezza di un file:

`ls {{[-lZ|-l --context]}} {{percorso/del/file}}`

- Cambia il contesto di sicurezza di un file usandone un'altro come riferimento:

`chcon --reference {{file_di_riferimento}} {{file}}`

- Cambia l'intero contesto di sicurezza SELinux di un file:

`chcon {{utente}}:{{ruolo}}:{{tipo}}:{{range/livello}} {{file}}`

- Cambia solo l'utente di un contesto di sicurezza SELinux:

`chcon {{[-u|--user]}} {{utente}} {{file}}`

- Cambia solo il ruolo di un contesto di sicurezza SELinux:

`chcon {{[-r|--role]}} {{ruolo}} {{file}}`

- Cambia solo il tipo di un contesto di sicurezza SELinux:

`chcon {{[-t|--type]}} {{tipo}} {{file}}`

- Cambia solo il range/livello di un contesto di sicurezza SELinux:

`chcon {{[-l|--range]}} {{range/livello}} {{file}}`
