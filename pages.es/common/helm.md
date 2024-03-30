# helm

> Helm es un gestor de paquetes para Kubernetes.
> Algunos subcomandos como `helm install` tiene su propia documentación de uso.
> Más información: <https://helm.sh/>.

- Crea un chart de helm:

`helm create {{nombre_del_chart}}`

- Añade un nuevo repositorio de helm:

`helm repo add {{nombre_del_repositorio}}`

- Lista de repositorios de helm:

`helm repo list`

- Actualiza los repositorios de helm:

`helm repo update`

- Elimina un repositorio de helm:

`helm repo remove {{nombre_del_repositorio}}`

- Instala un chart de helm:

`helm install {{nombre}} {{nombre_del_repositorio}}/{{nombre_del_chart}}`

- Descarga un chart de helm como un archivo tar:

`helm get {{nombre_del_lanzamiento_del_chart}}`

- Actualiza las dependencias de helm:

`helm dependency update`
