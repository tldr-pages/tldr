# vite-node

> Execute TypeScript and ESM files in Node.js powered by Vite transforms.
> More information: <https://github.com/vitest-dev/vitest/tree/main/packages/vite-node>.

- Execute a TypeScript or JavaScript file using Vite transforms:

`vite-node {{path/to/file.ts}}`

- Run a file in watch mode, re-executing automatically when dependencies change:

`vite-node --watch {{path/to/file.ts}}`

- Execute a script using a custom Vite configuration file:

`vite-node --config {{path/to/vite.config.ts}} {{path/to/file.ts}}`
