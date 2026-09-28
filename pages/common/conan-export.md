# conan export

> Export a recipe to the Conan package cache without building or installing it.
> More information: <https://docs.conan.io/2/reference/commands/export.html>.

- Export the recipe in the current directory to the cache:

`conan export`

- Export a recipe from a specific folder, overriding the package name and/or version:

`conan export {{path/to/recipe_folder}} --name={{name}} --version={{version}}`

- Mark the exported recipe as a build-requires package:

`conan export {{path/to/recipe_folder}} --build-require`

- Print the exported reference in JSON format:

`conan export {{path/to/recipe_folder}} --format=json`
