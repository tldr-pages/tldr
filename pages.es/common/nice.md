# nice

> Ejecuta un programa con una prioridad de programación personalizada (niceness).
> Los valores de niceness van desde -20 (la prioridad más alta) hasta 19 (la más baja).
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/nice-invocation.html>.

- Inicia un programa con la prioridad modificada:

`nice -{{valor_de_niceness}} {{comando}}`

- Defina la prioridad con una opción explícita:

`nice {{[-n|--adjustment]}} {{valor_de_niceness}} {{comando}}`
