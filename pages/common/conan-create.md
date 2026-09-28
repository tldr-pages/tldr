# conan create

> Generate the binary of a package from its recipe and add it, along with the recipe, to the Conan cache.
> More information: <https://docs.conan.io/2/reference/commands/create.html>.

- Build and package the recipe in the given folder, overriding its name and/or version:

`conan create {{path/to/recipe_folder}} --name={{name}} --version={{version}}`

- Build from source all dependencies that don't have a suitable binary:

`conan create {{path/to/recipe_folder}} --build=missing`

- Create the package using a specific profile:

`conan create {{path/to/recipe_folder}} -pr={{profile_name}}`

- Skip running the `test_package` folder:

`conan create {{path/to/recipe_folder}} --test-folder=""`
