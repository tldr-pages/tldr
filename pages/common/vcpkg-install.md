# vcpkg install

> Install C and C++ library packages with `vcpkg`.
> More information: <https://learn.microsoft.com/vcpkg/commands/install>.

- Install one or more packages:

`vcpkg install {{package1 package2 ...}}`

- Install a package for a specific triplet:

`vcpkg install {{package}}:{{x64-windows}}`

- Install all packages listed in the `vcpkg.json` manifest:

`vcpkg install`
