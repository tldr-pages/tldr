# pip

> Gestor de paquetes de Python.
> Algunos subcomandos, como `install`, cuentan con su propia documentación de uso.
> Más información: <https://pip.pypa.io/en/stable/cli/pip/>.

- Instala un paquete (vea `pip install` para ver más ejemplos de instalación):

`pip install {{paquete}}`

- Instala un paquete en el directorio del usuario en lugar de su ubicación predeterminada en todo el sistema:

`pip install --user {{paquete}}`

- Actualiza un paquete:

`pip install {{[-U|--upgrade]}} {{paquete}}`

- Desinstala un paquete:

`pip uninstall {{paquete}}`

- Guarda los paquetes instalados en un archivo:

`pip freeze > {{requirements.txt}}`

- Muestra una lista de los paquetes instalados:

`pip list`

- Muestra información sobre un paquete instalado:

`pip show {{package}}`

- Instala paquetes desde un archivo:

`pip install {{[-r|--requirement]}} {{requirements.txt}}`
