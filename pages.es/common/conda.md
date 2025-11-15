# conda

> Gestión de paquetes, dependencias y entornos para cualquier lenguaje de programación.
> Algunos subcomandos, como `create`, tienen su propia documentación de uso.
> Más información: <https://docs.conda.io/projects/conda/en/latest/commands/index.html>.

- Crea un nuevo entorno e instala en él los paquetes indicados:

`conda create {{[-n|--name]}} {{nombre_del_entorno}} {{python=3.9 matplotlib}}`

- Lista todos los entornos:

`conda info {{[-e|--envs]}}`

- Activa un entorno:

`conda activate {{nombre_del_entorno}}`

- Desactiva un entorno:

`conda deactivate`

- Elimina un entorno (remueve todos los paquetes):

`conda remove {{[-n|--name]}} {{nombre_del_entorno}} --all`

- Instala paquetes en el entorno actual:

`conda install {{python=3.4 numpy}}`

- Lista los paquetes instalados en el entorno actual:

`conda list`

- Elimina paquetes no usados y cachés:

`conda clean {{[-a|--all]}}`
