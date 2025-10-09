# az container

> Administra instancias de Azure Container.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/container>.

- Crea un contenedor en un grupo de contenedores:

`az container create {{[-g|--resource-group]}} {{grupo_de_recursos}} {{[-n|--name]}} {{nombre}} --image {{nombre_de_la_imagen}} {{[-os|--os-type]}} {{windows|linux}} --cpu {{número_de_núcleos_del_CPU}} --memory {{capacidad_de_memoria_en_GB}}`

- Ejecuta un comando desde un contenedor en ejecución dentro de un grupo de contenedores:

`az container exec {{[-g|--resource-group]}} {{grupo_de_recursos}} {{[-n|--name]}} {{nombre_del_grupo_de_contenedores}} --exec-command "{{comando}}"`

- Examina los registros de un contenedor en un grupo de contenedores:

`az container logs {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_de_recursos}}`

- Visualiza los detalles de un grupo de contenedores:

`az container show {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_de_recursos}}`

- Inicia todos los contenedores de un grupo de contenedores:

`az container start {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_de_recursos}}`

- Detiene todos los contenedores de un grupo de contenedores:

`az container stop {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_de_recursos}}`

- Elimina un grupo de contenedores:

`az container delete {{[-n|--name]}} {{nombre}} {{[-g|--resource-group]}} {{grupo_de_recursos}}`
