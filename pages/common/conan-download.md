# conan-download

> Download packages from a remote server to the local cache, without installing them or their transitive dependencies.
> More information: <https://docs.conan.io/2/reference/commands/download.html>.

- Download a package and all its binaries from a specific remote:

`conan download {{recipe}}/{{version}}:* --remote {{remote}}`

- Download only the recipe, without any binary packages:

`conan download {{recipe}}/{{version}} --only-recipe --remote {{remote}}`

- Download only the binaries matching a query:

`conan download {{recipe}}/{{version}} --package-query "{{os=Windows AND (arch=x86 OR compiler=gcc)}}" --remote {{remote}}`

- Download all packages listed in a package list file:

`conan download --list {{package_list.json}}`

- Download the metadata matching a pattern, even for packages already present in the cache:

`conan download {{recipe}}/{{version}} --metadata {{metadata_pattern}} --remote {{remote}}`
