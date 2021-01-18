# cmake

> Cross-platform build, testing and packaging automation system.
> CMake uses own shell-like syntax and generates recipes for several build systems.
> More information: <https://cmake.org/cmake/help/latest/manual/cmake.1.html>.

- Generate a build recipe in the current directory with CMakeLists.txt from a project directory:

`cmake {{path/to/project_dir/}}`

- Build with the generated recipe in build_dir (artifacts go to build_dir):

`cmake --build {{path/to/build_dir/}}`

- Install the project:

`cmake --install {{path/to/build_dir/}}`

- Run a custom build target:

`cmake --build {{path/to/build_dir/}} --target {{target_name}}`
