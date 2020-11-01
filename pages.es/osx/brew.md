# brew

> Administrador de paquetes para macOS.
> Más información: <https://brew.sh>.

- Busca fórmulas y paquetes disponibles:

`brew search {{text}}`

- Instala la última versión estable de una fórmula (usa `--devel` para versiones de desarrollo):

`brew install {{formula}}`

- Muestra todas las fórmulas instaladas:

`brew list`

- Muestra fórmulas instaladas que no dependen de otras:

`brew leaves`

- Actualiza una fórmula instalada (si no se indica el nombre, se actualizan todas las fórmulas):

`brew upgrade {{formula}}`

- Actualiza a la última versión de Homebrew y todas sus fórmulas desde GitHub:

`brew update`

- Elimina versiones antiguas de fórmulas instaladas (si no se indica el nombre, se busca en todas las fórmulas):

`brew cleanup {{formula}}`

- Muestra información acerca de una fórmula (versión, ruta de instalación, dependencias, etc.):

`brew info {{formula}}`

- Verifica la instalación local de Homebrew en busca de problemas potenciales:

`brew doctor`
