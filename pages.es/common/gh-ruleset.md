# gh ruleset

> Gestiona los conjuntos de reglas de los repositorios de GitHub.
> Más información: <https://cli.github.com/manual/gh_ruleset>.

- Muestra todos los conjuntos de reglas del repositorio actual:

`gh {{[rs|ruleset]}} {{[ls|list]}}`

- Muestra todos los conjuntos de reglas de una organización específica:

`gh {{[rs|ruleset]}} {{[ls|list]}} {{[-o|--org]}} {{nombre_organización}}`

- Comprueba las reglas que se aplican a la rama actual:

`gh {{[rs|ruleset]}} check`

- Comprueba las reglas que se aplican a una rama específica en otro repositorio:

`gh {{[rs|ruleset]}} check {{nombre_de_la_rama}} {{[-R|--repo]}} {{propietario}}/{{repositorio}}`

- Selecciona y muestra de forma interactiva un conjunto de reglas para el repositorio actual:

`gh {{[rs|ruleset]}} view`

- Muestra un conjunto de reglas específico por su ID:

`gh {{[rs|ruleset]}} view {{ruleset_id}}`

- Muestra un conjunto de reglas a nivel de organización por su ID:

`gh {{[rs|ruleset]}} view {{ruleset_id}} {{[-o|--org]}} {{nombre_organización}}`

- Abre la lista de conjuntos de reglas de un repositorio específico en el navegador:

`gh {{[rs|ruleset]}} {{[ls|list]}} {{[-R|--repo]}} {{propietario}}/{{repositorio}} {{[-w|--web]}}`
