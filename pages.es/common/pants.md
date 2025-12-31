# pants

> Herramienta de flujo de trabajo rápida, escalable, fácil de usar y de código abierto.
> Más información: <https://www.pantsbuild.org/stable/docs/using-pants/command-line-help>.

- Lista todos los objetivos:

`pants list ::`

- Ejecuta todas las pruebas:

`pants test ::`

- Arregla, formatea y limpia sólo los archivos no comprometidos:

`pants --changed-since=HEAD fix fmt lint`

- Comprueba sólo los archivos no comprometidos y sus dependientes:

`pants --changed-since=HEAD --changed-dependents=transitive check`

- Crea un paquete distribuible para el objetivo especificado:

`pants package {{ruta/al/directorio:nombre-destino}}`

- Autogenera objetivos de archivo BUILD para nuevos archivos fuente:

`pants tailor ::`

- Muestra la ayuda:

`pants help`
