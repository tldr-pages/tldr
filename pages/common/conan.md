# conan

> The open source, decentralized, and cross-platform package manager to create and share all your native binaries.
> Some subcommands such as `install`, `create`, `profile`, `remote` have their own usage documentation.
> More information: <https://docs.conan.io/2/reference/commands.html>.

- Scaffold a new project from a template recipe, e.g. a CMake library:

`conan new {{cmake_lib}} -d name={{pkg_name}} -d version={{1.0}}`

- Auto-detect the host environment and create a `default` profile:

`conan profile detect`

- Install dependencies based on `conanfile.txt` or a `conanfile.py` recipe:

`conan install {{.}}`

- Install a package directly from the configured remotes:

`conan install --requires={{zlib/1.3.1}}`

- Install dependencies, building from source only when prebuilt binaries are missing:

`conan install {{.}} --build {{missing}}`

- Create a package from a `conanfile.py` recipe in the current directory:

`conan create {{.}}`

- Build a package locally from its recipe without creating it:

`conan build {{.}}`

- List locally cached packages matching a pattern:

`conan list {{pattern}}`

- List remotes:

`conan remote list`
