# conan-source

> Call the `source()` method of a recipe to download or copy the package's source code into the source folder.
> More information: <https://docs.conan.io/2/reference/commands/source.html>.

- Run the `source()` method of the recipe in the current folder:

`conan source`

- Run the `source()` method of a recipe located in a specific folder:

`conan source {{path/to/folder}}`

- Provide a package name and version when they are not declared in the recipe:

`conan source --name {{name}} --version {{version}}`
