# conan build

> Install dependencies and call the `build()` method of a recipe.
> More information: <https://docs.conan.io/2/reference/commands/build.html>.

- Build the package defined in the current directory:

`conan build {{.}}`

- Build the package and store the artifacts in a specific output folder:

`conan build {{.}} --of {{path/to/output_folder}}`

- Build the package using a specific profile:

`conan build {{.}} {{[-pr|--profile]}} {{profile_name}}`
