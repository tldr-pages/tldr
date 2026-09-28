# conan install

> Install or resolve the dependencies of a recipe or a `conanfile.txt` file, generating integration files for the build system.
> More information: <https://docs.conan.io/2/reference/commands/install.html>.

- Install the dependencies of the recipe or `conanfile.txt` in the current folder:

`conan install .`

- Install the dependencies of a specific manifest file into an output folder:

`conan install {{path/to/conanfile_txt}} --output-folder={{path/to/output_folder}}`

- Install a single package requirement and its dependencies:

`conan install --requires={{package_name}}/{{version}}`

- Build from source all dependencies that don't have a suitable binary:

`conan install . --build=missing`

- Install using a specific build profile in addition to the host profile:

`conan install . -pr:h={{host_profile}} -pr:b={{build_profile}}`
