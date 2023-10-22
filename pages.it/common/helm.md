# helm

> Helm è un gestore di pacchetti per Kubernetes.
> Alcuni comandi aggiuntivi, come `helm install`, hanno la propria documentazione.
> Maggiori informazioni: <https://helm.sh/>.

- Crea una helm chart:

`helm create {{nome_chart}}`

- Aggiungi un nuovo repository helm:

`helm repo add {{nome_repository}}`

- Elenca i repositories helm:

`helm repo list`

- Aggiorna i repositories helm:

`helm repo update`

- Cancella un repository helm:

`helm repo remove {{nome_repository}}`

- Installa una helm chart:

`helm install {{nome_chart}} {{nome_repository}}/{{nome_chart}}`

- Scarica una helm chart sottoforma di archivio tar:

`helm get {{nome_chart_rilasciata}}`

- Aggiorna le dipendenze helm:

`helm dependency update`
