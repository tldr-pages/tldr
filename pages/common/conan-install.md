# conan install

> Install the dependencies specified in a recipe or `conanfile.txt`.
> More information: <https://docs.conan.io/2/reference/commands/install.html>.

- Install dependencies for the current directory:

`conan install {{.}}`

- Install dependencies, building from source only when prebuilt binaries are missing:

`conan install {{.}} --build {{missing}}`

- Install dependencies using a specific profile:

`conan install {{.}} {{[-pr|--profile]}} {{profile_name}}`

- Install dependencies in Release mode:

`conan install {{.}} {{[-s|--settings]}} {{build_type=Release}}`

- Install dependencies into a specific output folder:

`conan install {{.}} --of {{path/to/output_folder}}`
