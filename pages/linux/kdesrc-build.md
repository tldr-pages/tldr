# kdesrc-build

> Easily build KDE components from its source repositories.
> More information: <https://invent.kde.org/sdk/kdesrc-build>.

- Initialize kdesrc-build:

`kdesrc-build --initial-setup`

- Build a KDE `component_name` and its dependencies from source:

`kdesrc-build {{component_name}}`

- Build a component without updating its local code:

`kdesrc-build --no-src {{component_name}}`
