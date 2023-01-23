# gcloud

> A Google Cloud Platform hivatalos CLI eszköze. További információk: <https://cloud.google.com/sdk/gcloud>.

- Az aktív konfiguráció összes tulajdonságának listázása:

`gcloud config list`

- Jelentkezzen be a Google-fiókba:

`gcloud auth login`

- Állítsa be az aktív projektet:

`gcloud config set project {{project_name}}`

- SSH-hozzáférés egy virtuális géppéldányhoz:

`gcloud compute ssh {{user}}@{{instance}}`

- Az összes Google Compute Engine-példány megjelenítése egy projektben. Alapértelmezés szerint az összes zóna példányai szerepelnek a listában:

`gcloud compute instances list`

- Frissítse a kubeconfig fájlt a megfelelő hitelesítő adatokkal, hogy a kubectl-t egy adott fürtre irányítsa a Google Kubernetes Engine-ben:

`gcloud container clusters get-credentials {{cluster_name}}`

- Az összes gcloud CLI komponens frissítése:

`gcloud components update`

- Súgó megjelenítése egy adott parancshoz:

`gcloud help {{command}}`
