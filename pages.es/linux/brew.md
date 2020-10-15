# brew

> Gestor de paquetes Homebrew para Linux.

- Buscar fórmulas disponibles:

`brew search {{texto}}`

- Instalar la última versión de una fómula (usar `--devel` para la versión de desarrollo):

`brew install {{formula}}`

- Listar todas las fórmulas instaladas:

`brew list`

- Actualizar una fórmula instalada (si no se indica ninguna, todas las fórmulas son actualizadas):

`brew upgrade {{formula}}`

- Actualiza a la última versión de Linuxbrew y de todas las fórmulas desde Github:

`brew update`

- Mostrar las fórmulas que tienen una versión más reciente disponible:

`brew outdated`

- Mostrar la información de una fórmula (versión, ruta de instalación, dependencias, etc.):

`brew info {{formula}}`

- Revisar la instalación local de Linuxbrew en busca de problemas potenciales:

`brew doctor`
