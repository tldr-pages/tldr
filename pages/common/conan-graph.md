# conan graph

> Compute and analyze a dependency graph without installing or building binaries.
> More information: <https://docs.conan.io/2/reference/commands/graph.html>.

- Print the dependency graph of the conanfile in the current directory:

`conan graph info`

- Compute the graph for a specific package reference and print it as JSON:

`conan graph info --requires={{package_name}}/{{version}} --format=json`

- Compute the order in which the packages of a graph must be built:

`conan graph build-order {{path/to/conanfile}}`

- Explain dependency graph problems, such as missing binaries and closest alternatives:

`conan graph explain {{path/to/conanfile}}`
