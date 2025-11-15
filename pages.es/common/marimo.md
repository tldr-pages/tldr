# marimo

> Un entorno de cuaderno computacional Python reactivo.
> Combina características de Jupyter, Streamlit y otras herramientas de cuaderno computacional con ejecución reactiva.
> Más información: <https://docs.marimo.io/cli>.

- Crea o edita cuadernos iniciando un servidor marimo:

`marimo edit`

- Inicia un servidor marimo en un puerto específico sin lanzar un navegador:

`marimo edit {{[-p|--port]}} {{número_de_puerto}} --headless`

- Edita un cuaderno específico:

`marimo edit {{ruta/al/cuaderno.py}}`

- Ejecuta un cuaderno marimo como una aplicación en modo de sólo lectura:

`marimo run {{ruta/a/cuaderno.py}}`

- Inicia un tutorial interactivo para aprender marimo:

`marimo tutorial {{intro|components|dataflow|io}}`

- Muestra la ayuda específica del comando:

`marimo {{edit|run|tutorial|config|new|...}} --help`
