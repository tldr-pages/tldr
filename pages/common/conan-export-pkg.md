# conan export-pkg

> Create a package in the Conan cache directly from pre-compiled binaries, without building.
> More information: <https://docs.conan.io/2/reference/commands/export-pkg.html>.

- Export pre-built binaries from the current directory using the recipe found there:

`conan export-pkg`

- Export binaries from a specific recipe folder, overriding the package name and/or version:

`conan export-pkg {{path/to/recipe_folder}} --name={{name}} --version={{version}}`

- Use a specific profile when computing the package ID:

`conan export-pkg {{path/to/recipe_folder}} -pr={{profile_name}}`

- Skip installing the binaries of the dependencies:

`conan export-pkg {{path/to/recipe_folder}} {{[-sb|--skip-binaries]}}`
