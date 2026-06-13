# bosh

> Strumento da linea di comando per distribuire e gestire director BOSH.
> Maggiori informazioni: <https://bosh.io/docs/cli-v2/>.

- Crea un alias locale per un director:

`bosh alias-env {{nome_ambiente}} {{[-e|--environment]}} {{indirizzo_ip|url}} --ca-cert {{certificato_ca}}`

- Elenca ambienti:

`bosh environments`

- Esegui il login al director:

`bosh login {{[-e|--environment]}} {{ambiente}}`

- Elenca deployment (distribuzioni):

`bosh {{[-e|--environment]}} {{ambiente}} deployments`

- Elenca le macchine virtuali in un ambiente:

`bosh {{[-e|--environment]}} {{ambiente}} vms {{[-d|--deployment]}} {{deployment}}`

- Avvia una sessione SSH in una macchina virtuale:

`bosh {{[-e|--environment]}} {{ambiente}} ssh {{macchina_virtuale}} {{[-d|--deployment]}} {{deployment}}`

- Carica una stemcell:

`bosh {{[-e|--environment]}} {{ambiente}} upload-stemcell {{file_stemcell|url}}`

- Mostra la configurazione cloud attuale:

`bosh {{[-e|--environment]}} {{ambiente}} cloud-config`
