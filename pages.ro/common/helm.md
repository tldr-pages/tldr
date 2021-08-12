# helm

> Helm este manager de pachete pentru Kubernetes.
> Mai multe informaţii: <https://helm.sh/>

- Creați o diagramă Helm:

`helm create {{chart_name}}`

- Adăugați un nou depozit cârma:

`helm repo add {{repo_name}}`

- Lista depozitelor cârmei:

`helm repo list`

- Actualizarea depozitelor cârmei:

`helm repo update`

- Şterge un depozit de cârmă:

`helm repo remove {{repo_name}}`

- Instalați o diagramă Helm:

`helm install {{repo_name}}/{{chart_name}}`

- Descarcă diagrama Helm ca o arhivă de gudron:

`helm get {{chart_release_name}}`

- Actualizarea dependențelor cârmei:

`helm dependency update`
