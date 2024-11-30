# wine

> Ejecuta programas de Windows en sistemas basados en Unix.
> Más información: <https://wiki.winehq.org/>.

- Ejecuta un programa específico dentro del ambiente `wine`:

`wine {{comando}}`

- Ejecuta un programa específico en segundo plano (background):

`wine start {{comando}}`

- Instala/desinstala un paquete MSI:

`wine msiexec /{{i|x}} {{ruta/al/package.msi}}`

- Ejecuta `File Explorer`, `Notepad`, o `WordPad`:

`wine {{explorer|notepad|write}}`

- Ejecuta `Registry Editor`, `Control Panel` o `Task Manager`:

`wine {{regedit|control|taskmgr}}`

- Ejecuta la herramienta de configuración:

`wine winecfg`
