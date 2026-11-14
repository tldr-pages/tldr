# taze

> Modern CLI tool that keeps Node.js dependencies fresh across single packages and monorepos.
> More information: <https://github.com/antfu-collective/taze>.

- Check for outdated dependencies within the allowed semver range:

`taze`

- Check for major version updates across all dependencies:

`taze major`

- Write updated dependency versions directly to package manifest files:

`taze -w`

- Check dependencies recursively across all packages in a monorepo:

`taze -r`
