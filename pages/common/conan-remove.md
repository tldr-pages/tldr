# conan-remove

> Remove recipes or packages from the local cache or from a remote.
> More information: <https://docs.conan.io/2/reference/commands/remove.html>.

- Remove a recipe and all its binaries from the local cache, asking for confirmation:

`conan remove {{recipe}}/{{version}}`

- Remove without requesting confirmation:

`conan remove {{recipe}}/{{version}} --confirm`

- Remove only the binaries matching a query, keeping the recipe itself:

`conan remove {{recipe}}/{{version}} --package-query "{{os=Windows AND (arch=x86 OR compiler=gcc)}}"`

- Remove a recipe from a remote server:

`conan remove {{recipe}}/{{version}} --remote {{remote}}`

- Preview which items would be removed without actually removing anything:

`conan remove {{recipe}}/{{version}} --dry-run`

- Remove recipes and binaries that have not been used recently, e.g. in the last 30 days:

`conan remove --lru {{30d}}`
