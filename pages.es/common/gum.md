# gum

> Produce guiones glamorosos para el intérprete de comando.
> Más información: <https://github.com/charmbracelet/gum#tutorial>.

- Ofrece varias opciones para elegir una y la imprime en `stdout`:

`gum choose "{{opción_1}}" "{{opción_2}}" "{{opción_3}}"`

- Muestra una entrada de texto interactiva para que el usuario introduzca una cadena con un texto indicativo (placeholder) específico:

`gum input --placeholder "{{valor}}"`

- Abre un aviso de confirmación interactivo y sale con `<0>` o `<1>`:

`gum confirm "{{¿Continuar?}}" --default=false --affirmative "{{Sí}}" --negative "{{No}}" {{&& echo "Seleccionó Sí" || echo "Seleccionó No"}}`

- Muestra un spinner con un texto acompañante mientras se ejecuta una orden:

`gum spin --spinner {{dot|line|minidot|jump|pulse|points|globe|moon|monkey|meter|hamburger}} --title "{{cargando...}}" -- {{orden}}`

- Formatea texto para incluir emojis:

`gum format -t {{emoji}} "{{:smile: :heart: hola}}"`

- Solicita texto de varias líneas interactivamente (`<Ctrl d>` para salvar) y escribir en `datos.txt`:

`gum write > {{datos.txt}}`
