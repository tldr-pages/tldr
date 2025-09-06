# incus

> Contenedor de sistemas y gestor de máquinas virtuales moderno, seguro y potente.
> Más información: <https://linuxcontainers.org/incus/docs/main>.

- Lista todos los contenedores y máquinas virtuales (tanto en ejecución como detenidas):

`incus list`

- Crea un contenedor a partir de una imagen, con un nombre personalizado:

`incus create {{imagen}} {{nombre_del_contenedor}}`

- Inicia o detiene un contenedor existente:

`incus {{start|stop}} {{nombre_del_contenedor}}`

- Abre un intérprete de comandos dentro de un contenedor en ejecución:

`incus shell {{nombre_del_contenedor}}`

- Elimina un contenedor detenido:

`incus delete {{nombre_del_contenedor}}`

- Extrae una imagen de un repositorio de imágenes (remoto) al local:

`incus copy {{remoto}}:{{imagen}} local:{{nombre_de_imagen_personalizada}}`

- Lista todas las imágenes disponibles en el repositorio oficial `images:` remoto:

`incus image list images:`

- Lista todas las imágenes ya descargadas en el remoto `local:`:

`incus image list local:`
