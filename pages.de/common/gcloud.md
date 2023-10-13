# gcloud

> Das offizielle CLI-Tool für die Google Cloud Platform.
> Weitere Informationen: https://cloud.google.com/sdk/gcloud.

- Alle Eigenschaften in deiner aktiven Konfiguration auflisten:

`gcloud config list`

- Bei deinem Google-Konto anmelden:

`gcloud auth login`

- Das aktive Projekt festlegen:

`gcloud config set project {{Projektname}}`

- Eine SSH-Verbindung zu einer virtuellen Maschineninstanz herstellen:

`gcloud compute ssh {{Benutzer}}@{{Instanz}}`

- Alle Google Compute Engine-Instanzen in einem Projekt anzeigen. Instanzen aus allen Zonen werden standardmäßig aufgelistet:

`gcloud compute instances list`

- Eine kubeconfig-Datei mit den entsprechenden Anmeldeinformationen aktualisieren, um kubectl auf einen bestimmten Cluster in Google Kubernetes Engine auszurichten:

`gcloud container clusters get-credentials {{Clustername}}`

- Alle gcloud CLI-Komponenten aktualisieren:

`gcloud components update`

- Zeige Hilfe für einen bestimmten Befehl an:

`gcloud help {{Befehl}}`
