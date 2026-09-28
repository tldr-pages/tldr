# conan-new

> Create a new example recipe and source files from a built-in or user-provided template.
> More information: <https://docs.conan.io/2/reference/commands/new.html>.

- Generate a minimal example recipe (`conanfile.py`) in the current directory:

`conan new`

- Generate a new CMake library project from the `cmake_lib` template, filling in the template arguments:

`conan new cmake_lib --define name={{recipe_name}} --define version={{version}}`

- Generate the files into a specific output folder instead of the current directory:

`conan new cmake_exe --define name={{recipe_name}} --define version={{version}} --output {{path/to/folder}}`

- Overwrite files that already exist without asking:

`conan new meson_lib --define name={{recipe_name}} --define version={{version}} --force`

- Generate a project from a custom template stored in a folder of the Conan home:

`conan new {{path/to/custom/template}} --define {{key=value}}`
