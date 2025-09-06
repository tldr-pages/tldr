# kdesrc-build

> Easily build KDE components from its source repositories.
> More information: <https://docs.kde.org/trunk5/en/kdesrc-build/kdesrc-build/index.html>.

- Initialize `kdesrc-build`:

`kdesrc-build --initial-setup`

- Compile a KDE component and its dependencies from source:

`kdesrc-build {{component_name}}`

- Compile a component without updating its local code and without compiling its dependencies:

`kdesrc-build --no-src --no-include-dependencies {{component_name}}`

- Refresh the build directories before compiling:

`kdesrc-build --refresh-build {{component_name}}`

- Resume compilation from a specific dependency:

`kdesrc-build --resume-from {{dependency_component}} {{component_name}}`

- Run a component with a specified executable name:

`kdesrc-build --run --exec {{executable_name}} {{component_name}}`

- Build all configured components:

`kdesrc-build`

- Use system libraries in place of a component if it fails to build:

`kdesrc-build --no-stop-on-failure {{component_name}}`
