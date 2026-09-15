# pw-container

> Esegue un programma in un nuovo contesto di sicurezza.
> Maggiori informazioni: <https://docs.pipewire.org/page_man_pw-container_1.html>.

- Crea un nuovo contesto di sicurezza e stampa il suo indirizzo socket su `stdout`:

`pw-container`

- Esegue un programma specifico in un nuovo contesto di sicurezza:

`pw-container {{comando}} {{argomento1 argomento2 ...}}`

- Esegue un programma, collegandosi a un'istanza PipeWire remota specifica:

`pw-container {{[-r|--remote]}} {{nome_istanza_remota}} {{comando}}`

- Esegue un programma in un nuovo contesto con proprietà specifiche usando un oggetto JSON:

`pw-container {{[-P|--properties]}} '{{{"chiave": "valore"}}}' {{comando}}`

- Mostra aiuto:

`pw-container {{[-h|--help]}}`
