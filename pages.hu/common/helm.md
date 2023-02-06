# helm

> A Helm egy csomagkezelő a Kubernetes számára. Néhány alparancsnak, mint például a `helm install`, saját használati dokumentációja van. További információ: [https://helm.sh/.](https://helm.sh/)

- Hozzon létre egy helm táblázatot:

`helm create {{chart_name}}`

- Adjon hozzá egy új helm tárolót:

`helm repo add {{repository_name}}`

- Helm tárolók listázása:

`helm repo list`

- Helm tárolók frissítése:

`helm repo update`

- Helm-tárhely törlése:

`helm repo remove {{repository_name}}`

- Kormánytérkép telepítése:

`helm install {{name}} {{repository_name}}/{{chart_name}}`

- A helm chart letöltése tar archívumként:

`helm get {{chart_release_name}}`

- A helm függőségek frissítése:

`helm dependency update`
