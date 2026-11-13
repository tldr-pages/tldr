# attw

> Are The Types Wrong: analyze npm package contents to detect TypeScript module resolution issues.
> More information: <https://github.com/arethetypeswrong/arethetypeswrong.github.io>.

- Pack the current directory and check its TypeScript types across all resolution modes:

`attw --pack .`

- Check a published npm package tarball:

`attw {{path/to/package.tgz}}`

- Output the analysis results in a specific format:

`attw --pack . --format {{table|table-flipped|ascii|json}}`

- Run checks using a specific configuration profile:

`attw --pack . --profile {{strict|node16|esm-only}}`
