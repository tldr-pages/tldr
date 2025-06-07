# kde-builder

> Easily build KDE components from its source repositories.
> Drop-in replacement for `kdesrc-build`.
> More information: <https://kde-builder.kde.org/en/cmdline/cmdline-usage.html>.

- Initialize `kde-builder`:

`kde-builder --initial-setup`

- Compile a KDE component and its dependencies from the source (use `workspace` to compile Plasma desktop):

`kde-builder {{component_name1 component_name2 ...}}`

- Compile a component without updating its local code and without compiling its dependencies:

`kde-builder {{[-S|--no-src]}} {{[-D|--no-include-dependencies]}} {{component_name}}`

- Refresh the build directories before compiling:

`kde-builder {{[-r|--refresh-build]}} {{component_name}}`

- Resume compilation from a specific dependency:

`kde-builder {{[-f|--resume-from]}} {{dependency_component}} {{component_name}}`

- Run a component with a specified executable name:

`kde-builder --run {{executable_name}}`

- Build all configured components:

`kde-builder`

- Use system libraries in place of a component if it fails to build:

`kde-builder --no-stop-on-failure {{component_name}}`
