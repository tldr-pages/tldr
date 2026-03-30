# pip freeze

> Lista los paquetes instalados en formato de requisitos.
> Más información: <https://pip.pypa.io/en/stable/cli/pip_freeze/>.

- Lista los paquetes instalados:

`pip freeze`

- Escribe los paquetes instalados en el archivo `requirements.txt`:

`pip freeze > requirements.txt`

- Lista los paquetes instalados en un entorno virtual, excluyendo los instalados globalmente:

`pip freeze {{[-l|--local]}}`

- Lista los paquetes instalados en el directorio del usuario:

`pip freeze --user`

- Lista todos los paquetes, incluyendo `pip`, `distribute`, `setuptools` y `wheel` (se omiten por defecto):

`pip freeze --all`
