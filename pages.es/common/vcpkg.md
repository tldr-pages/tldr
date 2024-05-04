# vcpkg

> Gestor de paquetes para librerías C/C++.
> Nota: los paquetes no se instalan en el sistema. Para usarlos, necesitas decirle a tu sistema de compilación (por ejemplo CMake) que use `vcpkg`.
> Más información: <https://learn.microsoft.com/en-us/vcpkg/>.

- Construye y añade el paquete `libcurl` al entorno de `vcpkg`:

`vcpkg install curl`

- Construye y añade `zlib` usando la cadena de herramientas `emscripten`:

`vcpkg install --triplet=wasm32-emscripten zlib`

- Busca un paquete:

`vcpkg search {{nombre_del_paquete}}`

- Configura un proyecto CMake para utilizar los paquetes de `vcpkg`:

`cmake -B build -DCMAKE_TOOLCHAIN_FILE={{ruta/al/directorio_de_instalación_vcpkg}}/scripts/buildsystems/vcpkg.cmake`
