# bosh

> Strumento da linea di comando per distribuire e gestire director BOSH.
> Maggiori informazioni: <https://bosh.io/docs/cli-v2/>.

- Crea un alias locale per un director:

`bosh alias-env {{nome_ambiente}} -e {{indirizzo_ip|url}} --ca-cert {{certificato_ca}}`

- Elenca ambienti:

`bosh environments`

- Esegui il login al director:

`bosh login -e {{ambiente}}`

- Elenca deployment (distribuzioni):

`bosh -e {{ambiente}} deployments`

- Elenca le macchine virtuali in un ambiente:

`bosh -e {{ambiente}} vms -d {{deployment}}`

- Avvia una sessione SSH in una macchina virtuale:

`bosh -e {{ambiente}} ssh {{macchina_virtuale}} -d {{deployment}}`

- Carica una stemcell:

`bosh -e {{ambiente}} upload-stemcell {{file_stemcell|url}}`

- Mostra la configurazione cloud attuale:

`bosh -e {{ambiente}} cloud-config`
