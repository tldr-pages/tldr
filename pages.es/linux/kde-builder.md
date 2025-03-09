# kde-builder

> Construye fácilmente componentes de KDE desde tus repositorios fuente.
> Sustituye a `kdesrc-build`.
> Más información: <https://kde-builder.kde.org/en/cmdline/cmdline-usage.html>.

- Inicializa `kde-builder`:

`kde-builder --generate-config && kde-builder --install-distro-packages`

- Compila un componente KDE y sus dependencias desde el código fuente:

`kde-builder {{nombre_componente}}`

- Compila un componente sin actualizar el código local y sin compilar sus [D]ependencias:

`kde-builder --no-src --no-include-dependencies {{nombre_componente}}`

- Actualiza [R] los directorios de compilación antes de compilar:

`kde-builder --refresh-build {{nombre_componente}}`

- Reanuda la compilación a partir de una dependencia determinada:

`kde-builder --resume-from {{componente_de_dependencia}} {{nombre_componente}}`

- Ejecuta un componente con un nombre de ejecutable determinado:

`kde-builder --run {{nombre_ejecutable}}`

- Construye todos los componentes configurados:

`kde-builder`

- Utiliza las bibliotecas del sistema en lugar de un componente si no se puede compilar:

`kde-builder --no-stop-on-failure {{nombre_componente}}`
