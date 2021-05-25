# cmake

> Cross-platform build automation system, that generates recipes for native build systems.
> More information: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Generate a build recipe in the current directory with `CMakeLists.txt` from a project directory:

`cmake {{path/to/project_directory}}`

- Generate a build recipe, with build type set to `Release` with CMake variable:

`cmake {{path/to/project_directory}} -D {{CMAKE_BUILD_TYPE=Release}}`

- Use a generated recipe in a given directory to build artifacts:

`cmake --build {{path/to/build_directory}}`

- Install the build artifacts into `/usr/local/` and strip debugging symbols:

`cmake --install {{path/to/build_directory}} --strip`

- Install the build artifacts using the custom prefix for paths:

`cmake --install {{path/to/build_directory}} --strip --prefix {{path/to/directory}}`

- Run a custom build target:

`cmake --build {{path/to/build_directory}} --target {{target_name}}`
