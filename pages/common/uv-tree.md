# uv tree

> Display project dependencies in a tree format.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-tree>.

- Show dependency tree for current environment:

`uv tree`

- Show dependency tree for all environments:

`uv tree --universal`

- Show dependency tree up to a certain depth:

`uv tree {{[-d|--depth]}} {{n}}`

- Show the latest available version for all outdated packages:

`uv tree --outdated`

- Exclude dependencies from the dev group:

`uv tree --no-dev`

- Show the inverted tree, so children are dependents instead of dependencies:

`uv tree --invert`
