# kde-builder

> Construye fácilmente componentes de KDE desde tus repositorios fuente.
> Sustituye a `kdesrc-build`.
> Más información: <https://kde-builder.kde.org/en/cmdline/supported-cmdline-params.html>.

- Inicializa `kde-builder`:

`kde-builder --initial-setup`

- Compila un componente KDE y sus dependencias desde el código fuente:

`kde-builder {{nombre_componente1 nombre_componente2 ...}}`

- Compila un componente sin actualizar el código local y sin compilar sus dependencias:

`kde-builder {{[-SD|--no-src --no-include-dependencies]}} {{nombre_componente}}`

- Actualiza los directorios de compilación antes de compilar:

`kde-builder {{[-r|--refresh-build]}} {{nombre_componente}}`

- Reanuda la compilación a partir de una dependencia determinada:

`kde-builder {{[-f|--resume-from]}} {{dependencia_componente}} {{nombre_componente}}`

- Ejecuta un componente con un nombre de ejecutable determinado:

`kde-builder --run {{nombre_ejecutable}}`

- Construye todos los componentes configurados:

`kde-builder --install-login-session-only`

- Utiliza las bibliotecas del sistema en lugar de un componente si no se puede compilar:

`kde-builder --no-stop-on-failure {{nombre_ejecutable}}`
