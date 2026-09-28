# conan editable

> Work with packages directly from a local folder instead of the Conan cache.
> More information: <https://docs.conan.io/2/reference/commands/editable.html>.

- Define a local recipe folder as the location of a package, so requirements resolve to that folder instead of the cache:

`conan editable add {{path/to/recipe_folder}}`

- List all packages currently in editable mode:

`conan editable list`

- Remove the editable mode for a package:

`conan editable remove {{path/to/recipe_folder}}`
