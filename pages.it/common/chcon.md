# chcon

> Cambia contesto di sicurezza SELinux di file o directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/chcon>.

- Mostra il contesto di sicurezza di un file:

`ls -lZ {{percorso/al/file}}`

- Cambia il contesto di sicurezza di un file usandone un'altro come riferimento:

`chcon --reference={{file_di_riferimento}} {{file}}`

- Cambia l'intero contesto di sicurezza SELinux di un file:

`chcon {{utente}}:{{ruolo}}:{{tipo}}:{{range/livello}} {{file}}`

- Cambia solo l'utente di un contesto di sicurezza SELinux:

`chcon -u {{utente}} {{file}}`

- Cambia solo il ruolo di un contesto di sicurezza SELinux:

`chcon -r {{ruolo}} {{file}}`

- Cambia solo il tipo di un contesto di sicurezza SELinux:

`chcon -t {{tipo}} {{file}}`

- Cambia solo il range/livello di un contesto di sicurezza SELinux:

`chcon -l {{range/livello}} {{file}}`
