# madge

> Generate module dependency graphs and find circular dependencies in CommonJS, AMD, and ES6 projects.
> More information: <https://github.com/pahen/madge>.

- List all circular dependencies starting from an entry file or directory:

`madge --circular {{src/index.ts}}`

- Show modules that no other module depends on (orphan modules):

`madge --orphans {{src/}}`

- Generate a visual SVG dependency graph (requires Graphviz):

`madge --image {{graph.svg}} {{src/index.ts}}`

- Print a summary of module dependencies in JSON format:

`madge --json {{src/index.ts}}`
