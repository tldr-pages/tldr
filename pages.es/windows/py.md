# py

> Lanzador de Python para Windows que se ejecuta con la versión de Python especificada.
> Vea también: `python`.
> Más información: <https://docs.python.org/using/windows.html#python-launcher-for-windows>.

- Inicia un REPL (shell interactivo), opcionalmente con argumentos soportados por `python` (como `-c`, `-m`, etc.):

`py {{argumentos_python}}`

- Ejecuta un archivo Python específico:

`py {{ruta/al/archivo.py}}`

- Ejecuta una versión específica de Python. Si falta la versión y la variable de entorno `PYLAUNCHER_ALLOW_INSTALL` está configurada, instalar automáticamente a través de Microsoft Store o Winget:

`py {{-2|-3.7|...}}`

- Lista las versiones de Python instaladas:

`py --list`
