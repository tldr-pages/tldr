# gcloud

> Det officielle CLI værktøj for Google Cloud Platform.
> Mere information: <https://cloud.google.com/sdk/gcloud>.

- List alle aktive konfigurationer:

`gcloud config list`

- Login på en Google account:

`gcloud auth login`

- Sæt et GCP project som standard:

`gcloud config set project {{project_name}}`

- SSH ind til en virtuel maskine:

`gcloud compute ssh {{user}}@{{instance}} `

- Vis et overblik af alle Google Compute Engine instanser i et project. Instanser fra alle zoner er listet som standard:

`gcloud compute instances list`

- Vis hjælp for en command:

`gcloud help {{command}}`
