# gcloud

> La herramienta de línea de comandos oficial de Google Cloud Platform.
> Más información: <https://cloud.google.com/sdk/gcloud>.

- Listar todas las propiedades en la configuración activa:

`gcloud config list`

- Iniciar sesión en la cuenta de Google:

`gcloud auth login`

- Establecer el proyecto activo:

`gcloud config set project {{nombre_del_proyecto}}`

- SSH a una instancia de máquina virtual:

`gcloud compute ssh {{usuario}}@{{instancia}}`

- Mostrar todas las instancias de Google Compute Engine en un proyecto. Por defecto, se listan instancias de todas las zonas:

`gcloud compute instances list`

- Actualizar un archivo kubeconfig con las credenciales apropiadas para apuntar kubectl a un cluster específico en Google Kubernetes Engine:

`gcloud container clusters get-credentials {{nombre_del_cluster}}`

- Actualizar todos los componentes de la CLI de gcloud:

`gcloud components update`

- Mostrar ayuda para un comando dado:

`gcloud help {{comando}}`
