# vcpkg depend-info

> Display the transitive dependencies of packages, regardless of whether they are installed.
> More information: <https://learn.microsoft.com/en-us/vcpkg/commands/depend-info>.

- List the transitive dependencies of a package, sorted topologically by increasing depth:

`vcpkg depend-info {{package_name}}`

- Display the dependencies as a tree:

`vcpkg depend-info {{package_name}} --format=tree`

- Generate the dependency graph in another format (`list`, `tree`, `dot`, `dgml`, or `mermaid`):

`vcpkg depend-info {{package_name}} --format={{dot|dgml|mermaid}}`

- Limit the displayed recursion depth (use `-1` for no limit):

`vcpkg depend-info {{package_name}} --max-recurse={{depth}}`

- Sort the list output lexicographically, topologically, or by decreasing depth:

`vcpkg depend-info {{package_name}} --sort={{lexicographical|topological|reverse}}`
