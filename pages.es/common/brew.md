# brew

> Administrador de paquetes para macOS y Linux.
> Más información: <https://brew.sh>.

- Instala la última versión estable de una fórmula (usar `--devel` para versiones de desarrollo):

`brew install {{formula}}`

- Lista todas las fórmulas y casks instaladas:

`brew list`

- Actualiza una fórmula o cask instalada (si no se indica ninguna, todas las fórmulas/casks se actualizan):

`brew upgrade {{formula}}`

- Trae la versión más reciente de Homebrew y todas sus fórmulas y casks desde el repositorio fuente de Homebrew:

`brew update`

- Muestra las fórmulas y casks que tienen una versión más reciente disponible:

`brew outdated`

- Busca fórmulas (por ej. paquetes) y casks (por ej. paquetes nativos) disponibles:

`brew search {{texto}}`

- Muestra la información de una fórmula o un cask (versión, ruta de instalación, dependencias, etc.):

`brew info {{formula}}`

- Revisa la instalación local de Homebrew en busca de problemas potenciales:

`brew doctor`
