# vcpkg

> Package manager for C/C++ libraries.
> Note: Packages are not installed in the system. To use them, you need to tell your build system (e.g. CMake) to use `vcpkg`.
> More information: <https://learn.microsoft.com/vcpkg/>.

- Build and add `curl` to the `vcpkg` environment:

`vcpkg install curl`

- Build and add `zlib` using the `emscripten` toolchain:

`vcpkg install --triplet=wasm32-emscripten zlib`

- Install all packages listed in the `vcpkg.json` manifest:

`vcpkg install`

- Add a port to the `vcpkg.json` manifest:

`vcpkg add port {{package}}`

- Remove a package from the `vcpkg` environment:

`vcpkg remove {{package}}`

- List installed packages:

`vcpkg list`

- Search for a package:

`vcpkg search {{pkg_name}}`

- Configure a CMake project to use `vcpkg` packages:

`cmake -B build -DCMAKE_TOOLCHAIN_FILE={{path/to/vcpkg_install_directory}}/scripts/buildsystems/vcpkg.cmake`
