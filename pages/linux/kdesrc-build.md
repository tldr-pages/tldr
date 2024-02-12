# kdesrc-build

> Easily build KDE components from its source repositories.
> More information: <https://invent.kde.org/sdk/kdesrc-build>.

- Initialize `kdesrc-build`:

`kdesrc-build --initial-setup`

- Compile a KDE component and its dependencies from source:

`kdesrc-build {{component_name}}`

- Compile a component without updating its local code and without compiling its dependencies:

`kdesrc-build --no-src --no-include-dependencies {{component_name}}`

- Refresh the build directories before compiling:

`kdesrc-build --refresh-build {{component_name}}`

- Resume compilation from a specific dependency:

`kdesrc-build --resume-from={{dependency_component}} {{component_name}}`

- Print full compilation info:

`kdesrc-build --debug {{component_name}}`

- Build all configured components:

`kdesrc-build`
