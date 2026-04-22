# pipenv

> Flujo de trabajo de desarrollo de Python sencillo y unificado.
> Gestiona los paquetes y el entorno virtual de un proyecto.
> Más información: <https://pypi.org/project/pipenv>.

- Crea un nuevo proyecto:

`pipenv`

- Crea un nuevo proyecto con Python 3:

`pipenv --three`

- Instala un paquete:

`pipenv install {{paquete}}`

- Instala todas las dependencias de un proyecto:

`pipenv install`

- Instala todas las dependencias de un proyecto (incluidos los paquetes de desarrollo):

`pipenv install --dev`

- Desinstala un paquete:

`pipenv uninstall {{paquete}}`

- Inicia un intérprete de comandos dentro del entorno virtual creado:

`pipenv shell`

- Genera un archivo `requirements.txt` (lista de dependencias) para un proyecto:

`pipenv lock --requirements`
