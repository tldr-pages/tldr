# conan create

> Create a package from a `conanfile.py` recipe.
> More information: <https://docs.conan.io/2/reference/commands/create.html>.

- Create a package from the recipe in the current directory:

`conan create {{.}}`

- Create a package with a specific name and version:

`conan create {{.}} --name {{name}} --version {{version}}`

- Create a package with a specific user and channel:

`conan create {{.}} --user {{user}} --channel {{channel}}`
