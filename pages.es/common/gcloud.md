# gcloud

> La herramienta CLI oficial de Google Cloud Platform.
> Más información: <https://cloud.google.com/sdk/gcloud>.

- Lista todas las propiedades de la configuración activa:

`gcloud config list`

- Inicia sesión en la cuenta de Google:

`gcloud auth login`

- Establece como proyecto activo:

`gcloud config set project {{nombre_del_proyecto}}`

- SSH en una instancia de máquina virtual:

`gcloud compute ssh {{usuario}}@{{instancia}}`

- Muestra todas las instancias de Google Compute Engine de un proyecto. Por defecto, se muestran las instancias de todas las zonas:

`gcloud compute instances list`

- Actualiza un archivo kubeconfig con las credenciales adecuadas para apuntar kubectl a un clúster específico en Google Kubernetes Engine:

`gcloud container clusters get-credentials {{nombre_cluster}}`

- Actualiza todos los componentes de la CLI de gcloud:

`gcloud components update`

- Muestra la ayuda para un comando determinado:

`gcloud help {{comando}}`
