# numbat

> Una calculadora científica de tipado estático con soporte de primera clase para unidades físicas.
> Vea también: `qalc`, `bc`.
> Más información: <https://numbat.dev>.

- Inicia una sesión interactiva:

`numbat`

- [E]valúa una o más expresiones:

`numbat {{[-e|--expression]}} '{{2 hours + 30 minutes -> seconds}}'`

- Ejecuta un script de Numbat:

`numbat {{ruta/al/script.nbt}}`

- Entra en una sesión [i]nteractiva tras ejecutar un script o expresión:

`numbat {{[-i|--inspect-interactively]}} {{ruta/al/script.nbt}}`

- [N]o cargues el preludio de dimensiones y unidades predefinidas:

`numbat {{[-N|--no-prelude]}}`

- Genera un archivo de configuración predeterminado:

`numbat --generate-config`
