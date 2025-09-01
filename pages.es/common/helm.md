# helm

> Helm es un gestor de paquetes para Kubernetes.
> Algunos subcomandos como `install` tiene su propia documentación de uso.
> Más información: <https://helm.sh/docs/helm/>.

- Crea un chart de helm:

`helm create {{nombre_del_chart}}`

- Añade un nuevo repositorio de helm:

`helm repo add {{nombre_del_repositorio}}`

- Lista de repositorios de helm:

`helm repo {{[ls|list]}}`

- Actualiza los repositorios de helm:

`helm repo {{[up|update]}}`

- Elimina un repositorio de helm:

`helm repo {{[rm|remove]}} {{nombre_del_repositorio}}`

- Instala un chart de helm:

`helm install {{nombre}} {{nombre_del_repositorio}}/{{nombre_del_chart}}`

- Descarga un chart de helm como un archivo tar:

`helm get {{nombre_del_lanzamiento_del_chart}}`

- Actualiza las dependencias de helm:

`helm {{[dep|dependency]}} {{[up|update]}}`
