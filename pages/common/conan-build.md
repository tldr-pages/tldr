# conan build

> Build a package from a local recipe folder, without exporting it to the cache.
> More information: <https://docs.conan.io/2/reference/commands/build.html>.

- Run the generators and build the package in the given recipe folder:

`conan build {{path/to/recipe_folder}}`

- Build using a specific profile:

`conan build {{path/to/recipe_folder}} -pr={{profile_name}}`

- Build, also building from source any dependency without a ready binary:

`conan build {{path/to/recipe_folder}} --build=missing`
