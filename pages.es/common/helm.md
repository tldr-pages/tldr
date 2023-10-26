# helm

> Helm es un gestor de paquetes para Kubernetes.
> Algunos subcomandos como `helm install` tiene su propia documentación de uso.
> Mas información: <https://helm.sh/>.

- Crear un chart de helm:

`helm create {{nombre_del_chart}}`

- Añadir un nuevo repositorio de helm:

`helm repo add {{nombre_del_repositorio}}`

- Lista de repositorios de helm:

`helm repo list`

- Actualizar los repositorios de helm:

`helm repo update`

- Eliminar un repositorio de helm:

`helm repo remove {{nombre_del_repositorio}}`

- Instalar un chart de helm:

`helm install {{nombre}} {{nombre_del_repositorio}}/{{nombre_del_chart}}`

- Descargar un chart de helm como un archivo tar:

`helm get {{nombre_del_lanzamiento_del_chart}}`

- Actualizar las depencias de helm:

`helm dependency update`
