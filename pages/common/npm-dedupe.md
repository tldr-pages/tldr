# npm dedupe

> Reduce duplication in the `node_modules` directory.
> More information: <https://docs.npmjs.com/cli/commands/npm-dedupe>.

- Deduplicate packages in `node_modules`:

`npm dedupe`

- Follow `package-lock.json` or `npm-shrinkwrap.json` during deduplication:

`npm dedupe --lock`

- Run deduplication in strict mode:

`npm dedupe --strict`

- Skip optional/peer dependencies during deduplication:

`npm dedupe --omit {{optional|peer}}`

- Enable detailed logging for troubleshooting:

`npm dedupe --loglevel verbose`

- Limit deduplication to a specific package:

`npm dedupe {{package_name}}`
