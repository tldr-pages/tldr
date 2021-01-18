# cmake

> Cross-platform build, testing and packaging automation system.
> CMake uses its own shell-like syntax and generates recipes for many build systems.
> More information: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Generate a build recipe in the current directory with `CMakeLists.txt` from a project directory:

`cmake {{path/to/project_directory}}`

- Build artifacts with the generated recipe in `build_directory`:

`cmake --build {{path/to/build_directory}}`

- Install the build artifacts into /usr/local/ striping debugging symbols:

`cmake --install {{path/to/build_directory}} --strip --prefix /usr/local/`

- Run a custom build target:

`cmake --build {{path/to/build_dir/}} --target {{target_name}}`
