# gcloud

> Det officielle CLI værktøj for Google Cloud Platform.
> Mere information: <https://cloud.google.com/sdk/gcloud>.

- List alle aktive konfigurationer:

`gcloud config list`

- Login på en Google account:

`gcloud auth login`

- Sæt et GCP project som standard:

`gcloud config set project {{projekt_navn}}`

- SSH ind til en virtuel maskine:

`gcloud compute ssh {{bruger}}@{{instans}}`

- Vis et overblik af alle Google Compute Engine instanser i et project. Instanser fra alle zoner er listet som standard:

`gcloud compute instances list`

- Opdater en kube-konfiguratonsfil med de korrekte credentials, der peger kubectl mod et spesifikt cluster i Google Kubernetes Engine:

`gcloud container clusters get-credentials {{cluster_navn}}`

- Opdater all gcloud CLI komponenter:

`gcloud components update`

- Vis hjælp for en command:

`gcloud help {{kommando}}`
