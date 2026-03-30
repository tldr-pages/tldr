# pip

> Gestor de paquetes de Python.
> Algunos subcomandos como `install` tienen su propia documentación de uso.
> Más información: <https://pip.pypa.io/en/stable/cli/pip/>.

- Instala un paquete (consulta `pip install` para más ejemplos de instalación):

`pip install {{paquete}}`

- Instala un paquete en el directorio del usuario en lugar de la ubicación predeterminada del sistema:

`pip install --user {{paquete}}`

- Actualiza un paquete:

`pip install {{[-U|--upgrade]}} {{paquete}}`

- Desinstala un paquete:

`pip uninstall {{paquete}}`

- Guarda los paquetes instalados en un archivo:

`pip freeze > {{requirements.txt}}`

- Lista los paquetes instalados:

`pip list`

- Muestra información de un paquete instalado:

`pip show {{paquete}}`

- Instala paquetes desde un archivo:

`pip install {{[-r|--requirement]}} {{requirements.txt}}`
