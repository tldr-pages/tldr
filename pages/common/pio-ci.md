# pio ci

> Build PlatformIO projects with an arbitrary source code structure.
> This will create a new temporary project which the source code will be copied into.
> More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_ci.html>.

- Build a PlatformIO project in the default system temporary directory and delete it afterwards:

`pio ci {{path/to/project}}`

- Build a PlatformIO project and specify specific libraries:

`pio ci --lib {{path/to/library_directory}} {{path/to/project}}`

- Build a PlatformIO project and specify a specific board (`pio boards` lists all of them):

`pio ci --board {{board}} {{path/to/project}}`

- Build a PlatformIO project in a specific directory:

`pio ci --build-dir {{path/to/build_directory}} {{path/to/project}}`

- Build a PlatformIO project and don't delete the build directory:

`pio ci --keep-build-dir {{path/to/project}}`

- Build a PlatformIO project using a specific configuration file:

`pio ci --project-conf {{path/to/platformio.ini}}`
