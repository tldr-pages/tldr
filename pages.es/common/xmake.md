# xmake

> Una utilidad de compilación multiplataforma C & C++ basada en Lua.
> Más información: <https://xmake.io/#/getting_started>.

- Crea un proyecto Xmake C, consistente en un hello world y `xmake.lua`:

`xmake create {{[-l|--language]}} {{[c|clean]}} {{[-P|--project]}} {{nombre_del_proyecto}}`

- Construye y ejecuta un proyecto Xmake:

`xmake {{[b|build]}} {{[r|run]}}`

- Ejecuta directamente un objetivo Xmake compilado:

`xmake {{[r|run]}} {{nombre_del_objetivo}}`

- Configura los objetivos de compilación de un proyecto:

`xmake {{[f|config]}} {{[-p |--plat=]}}{{macosx|linux|iphoneos|...}} {{[-a |--arch=]}}{{x86_64|i386|arm64|...}} {{[-m |--mode=]}}{{debug|release}}`

- Instala el objetivo compilado en un directorio:

`xmake {{[i|install]}} {{[-o |--installdir=]}}{{ruta/al/directorio}}`
