# xmake

> Una utilidad de compilación multiplataforma C & C++ basada en Lua.
> Más información: <https://xmake.io/#/getting_started>.

- Crea un proyecto Xmake C, consistente en un hello world y `xmake.lua`:

`xmake create --language c -P {{nombre_del_proyecto}}`

- Construye y ejecuta un proyecto Xmake:

`xmake build run`

- Ejecuta directamente un objetivo Xmake compilado:

`xmake run {{nombre_del_objetivo}}`

- Configura los objetivos de compilación de un proyecto:

`xmake config --plat={{macosx|linux|iphoneos|...}} --arch={{x86_64|i386|arm64| ..}} --mode={{debug|release}}`

- Instala el objetivo compilado en un directorio:

`xmake install -o {{ruta/al/directorio}}`
