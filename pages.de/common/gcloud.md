# gcloud

> Das offizielle CLI-Tool für die Google Cloud Platform.
> Weitere Informationen: https://cloud.google.com/sdk/gcloud.

- Liste alle Eigenschaften der aktiven Konfiguration auf:

`gcloud config list`

- Mit einem Google-Konto anmelden:

`gcloud auth login`

- Lege das aktive Projekt fest:

`gcloud config set project {{Projektname}}`

- Stelle eine SSH-Verbindung zu einer virtuellen Maschineninstanz her:

`gcloud compute ssh {{Benutzer}}@{{Instanz}}`

- Zeige alle Google Compute Engine-Instanzen in einem Projekt an. Standardmäßig werden Instanzen aus allen Zonen aufgelistet:

`gcloud compute instances list`

- Aktualisiere eine kubeconfig-Datei mit den entsprechenden Anmeldeinformationen, um kubectl auf einen bestimmten Cluster in Google Kubernetes Engine auszurichten:

`gcloud container clusters get-credentials {{Clustername}}`

- Aktualisiere alle gcloud CLI-Komponenten:

`gcloud components update`

- Zeige Hilfe für einen bestimmten Befehl an:

`gcloud help {{Befehl}}`
