# kubectl logs

> Muestra los registros de los contenedores de un pod.
> Más información: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs>.

- Muestra los registros de un pod de un contenedor:

`kubectl logs {{nombre_del_pod}}`

- Muestra los registros de un contenedor especificado en un pod:

`kubectl logs {{[-c|--container]}} {{nombre_del_contenedor}} {{nombre_del_contenedor}}`

- Muestra los registros de todos los contenedores de un pod:

`kubectl logs --all-containers={{true}} {{nombre_del_contenedor}}`

- Transmite los registros del pod:

`kubectl logs {{[-f|--follow]}} {{nombre_del_pod}}`

- Muestra los registros de pods más recientes dado un tiempo relativo como `10s`, `5m` o `1h`:

`kubectl logs --since {{tiempo_relativo}} {{nombre_del_pod}}`

- Muestra los 10 registros más recientes de un pod:

`kubectl logs --tail {{10}} {{nombre_del_pod}}`

- Muestra todos los registros de un pod para un despliegue determinado:

`kubectl logs {{[deploy|deployment]}}/{{nombre_del_despliegue}}`
