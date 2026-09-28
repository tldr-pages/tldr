# conan-test

> Test a package by installing and building a test project from a `test_package` folder against the given package reference.
> More information: <https://docs.conan.io/2/reference/commands/test.html>.

- Test a package using the `test_package` folder in the current directory:

`conan test test_package {{recipe}}/{{version}}`

- Test a package with a specific profile:

`conan test {{path/to/test_package}} {{recipe}}/{{version}} --profile {{profile_name}}`

- Test a package, building missing dependencies from source instead of failing:

`conan test test_package {{recipe}}/{{version}} --build missing`

- Test a package resolved exclusively in the local cache, without contacting remotes:

`conan test test_package {{recipe}}/{{version}} --no-remote`
