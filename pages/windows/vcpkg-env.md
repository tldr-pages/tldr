# vcpkg env

> Create a clean `cmd` build environment matching the one vcpkg uses to build ports.
> Note: This command is only available on Windows.
> More information: <https://learn.microsoft.com/en-us/vcpkg/commands/env>.

- Start an interactive build environment session:

`vcpkg env`

- Run a single command inside the build environment and exit:

`vcpkg env "{{command}}"`

- Target a specific triplet when configuring the environment:

`vcpkg env --triplet={{triplet}} "{{command}}"`

- Prepend a folder of the triplet's installed tree to the session environment (`bin`, `debug-bin`, `include`, `tools`, or `python`):

`vcpkg env --{{bin|debug-bin|include|tools|python}} "{{command}}"`
