# pipenv

> Flujo de trabajo de desarrollo Python simple y unificado.
> Gestiona paquetes y el entorno virtual para un proyecto.
> Más información: <https://pypi.org/project/pipenv>.

- Crea un nuevo proyecto:

`pipenv`

- Crea un nuevo proyecto usando Python 3:

`pipenv --three`

- Instala un paquete:

`pipenv install {{paquete}}`

- Instala todas las dependencias de un proyecto:

`pipenv install`

- Instala todas las dependencias de un proyecto (incluyendo los paquetes de desarrollo):

`pipenv install --dev`

- Desinstala un paquete:

`pipenv uninstall {{paquete}}`

- Inicia un shell dentro del entorno virtual creado:

`pipenv shell`

- Genera un `requirements.txt` (lista de dependencias) para un proyecto:

`pipenv lock --requirements`
