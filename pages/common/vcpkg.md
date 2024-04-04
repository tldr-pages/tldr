# vcpkg

> Package manager for C/C++ libraries.
> Note: packages are not installed in the system. To use them, you need to tell your build system (e.g. CMake) to use `vckg`.
> More information: <https://learn.microsoft.com/en-us/vcpkg/>.

- Build and add package `libcurl` to the `vcpkg` environment:

`vcpkg install curl`

- Build and add `zlib` using the `emscripten` toolchain:

`vcpkg install --triplet=wasm32-emscripten zlib`

- Search for a package:

`vcpkg search {{pkg_name}}`

- Configure a CMake project to use `vcpkg` packages:

`cmake -B build -DCMAKE_TOOLCHAIN_FILE={{path/to/vcpkg_install_directory}}/scripts/buildsystems/vcpkg.cmake`
