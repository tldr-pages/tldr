# mamba

> Gestor de paquetes rápido y multiplataforma, diseñado como sustituto directo de conda.
> Algunos subcomandos, como `repoquery`, tienen su propia documentación de uso.
> Vea también: `conda`.
> Más información: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html>.

- Crea un nuevo entorno e instala los paquetes especificados en el mismo:

`mamba create {{[-n|--name]}} {{nombre_entorno}} {{python=3.10 matplotlib}}`

- Instala paquetes en el entorno actual, especificando el canal del paquete:

`mamba install {{[-c|--channel]}} {{conda-forge}} {{python=3.6 numpy}}`

- Actualiza todos los paquetes del entorno actual:

`mamba update {{[-a|--all]}}`

- Busca un paquete específico en todos los repositorios:

`mamba repoquery search {{numpy}}`

- Muestra todos los entornos:

`mamba info {{[-e|--envs]}}`

- Elimina los paquetes y archivos tarballs no utilizados de la caché:

`mamba clean {{[-pt|--packages --tarballs]}}`

- Activa un entorno:

`mamba activate {{nombre_del_entorno}}`

- Enumera todos los paquetes instalados en el entorno actualmente activado:

`mamba list`
