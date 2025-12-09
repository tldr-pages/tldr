# ruff check

> Un linter extremadamente rápido para Python. `check` es el comando predeterminado - se puede omitir en todas partes.
> Si no se especifican archivos o directorios, el directorio de trabajo actual se utiliza por defecto.
> Más información: <https://docs.astral.sh/ruff/linter>.

- Ejecuta el linter en los archivos o directorios dados:

`ruff check {{ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...}}`

- Aplica las correcciones sugeridas, modificando los archivos afectados:

`ruff check --fix`

- Ejecuta el linter y lo aplica de nuevo ante algún cambio:

`ruff check --watch`

- Solo habilita las reglas especificadas (o todas las reglas), ignorando el archivo de configuración:

`ruff check --select {{ALL|regla_de_código1,regla_de_código2,...}}`

- Además, habilita las reglas especificadas:

`ruff check --extend-select {{regla_de_código1,regla_de_código2,...}}`

- Desactiva las reglas especificadas:

`ruff check --ignore {{regla_de_código1,regla_de_código2,...}}`

- Ignora todas las violaciones existentes de una regla añadiendo las directivas "# noqa" a todas las líneas que la violan:

`ruff check --select {{regla_de_código}} --add-noqa`
