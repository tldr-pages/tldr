# attw

> Check TypeScript type definitions of an npm package for module resolution issues across bundlers and Node.js.
> More information: <https://github.com/arethetypeswrong/arethetypeswrong.github.io>.

- Pack the current directory and check its TypeScript types:

`attw --pack`

- Check an already-packed tarball file:

`attw {{path/to/package.tgz}}`

- Check a specific module resolution profile only:

`attw --pack --profile {{node16|esm-only|strict}}`

- Output the analysis results in JSON format:

`attw --pack --format {{json}}`
