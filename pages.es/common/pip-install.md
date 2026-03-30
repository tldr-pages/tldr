# pip install

> Instala paquetes de Python.
> Más información: <https://pip.pypa.io/en/stable/cli/pip_install/>.

- Instala uno o más paquetes:

`pip install {{paquete1 paquete2 ...}}`

- Actualiza todos los paquetes especificados a la última versión, instalando los que no estén presentes:

`pip install {{paquete1 paquete2 ...}} {{[-U|--upgrade]}}`

- Instala una versión específica de un paquete:

`pip install {{paquete}}=={{versión}}`

- Instala paquetes listados en un archivo:

`pip install {{[-r|--requirement]}} {{ruta/al/requirements.txt}}`

- Instala un paquete desde un archivo o directorio local:

`pip install {{ruta/al/archivo.whl|ruta/al/archivo.tar.gz|ruta/al/directorio}}`

- Instala un paquete desde un repositorio Git:

`pip install git+https://{{example.com}}/{{usuario}}/{{repositorio}}.git`

- Instala un paquete desde una fuente alternativa (URL o directorio) en lugar de PyPI:

`pip install {{[-f|--find-links]}} {{url|ruta/al/directorio}} {{paquete}}`

- Instala el paquete local del directorio actual en modo de desarrollo (editable):

`pip install {{[-e|--editable]}} .`
