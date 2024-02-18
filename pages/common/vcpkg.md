# vcpkg

> Package manager for C/C++ libraries.
> Note: packages are not installed in the system. To use them, you need to tell your build system (e.g. cmake) to use vckg.
> More information: <https://learn.microsoft.com/en-us/vcpkg/>.

- Build and add package libcurl to the vcpkg environment:

`vcpkg install curl`

- Build and add zlib with the emscripten toolchain:

`vcpkg install --triplet=wasm32-emscripten zlib`

- Search for a package:

`vcpkg search {{pkg_name}}`

- Configure a cmake project to use vcpkg packages (replace $VCPKG_ROOT with the install folder of vcpkg):

`cmake -B build -DCMAKE_TOOLCHAIN_FILE={{path/to/vcpkg_install_directory}}/scripts/buildsystems/vcpkg.cmake`
