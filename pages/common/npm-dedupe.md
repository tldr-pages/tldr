# npm dedupe

> Reduce duplication in the `node_modules` directory.
> More information: <https://docs.npmjs.com/cli/npm-dedupe>.

- Deduplicate packages in `node_modules`:

`npm {{[ddp|dedupe]}}`

- Follow `package-lock.json` or `npm-shrinkwrap.json` during deduplication:

`npm {{[ddp|dedupe]}} --lock`

- Run deduplication in strict mode:

`npm {{[ddp|dedupe]}} --strict`

- Skip optional/peer dependencies during deduplication:

`npm {{[ddp|dedupe]}} --omit {{optional|peer}}`

- Enable detailed logging for troubleshooting:

`npm {{[ddp|dedupe]}} --loglevel verbose`

- Limit deduplication to a specific package:

`npm {{[ddp|dedupe]}} {{package_name}}`
