# conan cache

> Perform file operations on the local Conan cache of recipes and packages.
> More information: <https://docs.conan.io/2/reference/commands/cache.html>.

- Show the cache folder path for a given package reference:

`conan cache path {{package_reference}}`

- Remove non-critical folders (source `-s`, build `-b`, downloads `-d`) from cached packages matching a pattern:

`conan cache clean {{pattern}} -s -b`

- Check the integrity of the local cache for the given references:

`conan cache check-integrity {{package_reference}}`

- Archive cached artifacts matching a pattern into a file:

`conan cache save {{package_name}}/{{version}}:* --file={{path/to/archive}}`
