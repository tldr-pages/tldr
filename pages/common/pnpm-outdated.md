# pnpm outdated

> Check for outdated packages.
> The check can be limited to a subset of the installed packages by providing arguments (patterns are supported).
> More information: <https://pnpm.io/cli/outdated>.

- Check for outdated packages:

`pnpm outdated`

- Check for outdated dependencies found in every workspace package:

`pnpm outdated -r`

- Filter outdated packages using a package selector:

`pnpm outdated --filter {{package_selector}}`

- List outdated packages [g]lobally:

`pnpm outdated --global`

- Print details of outdated packages:

`pnpm outdated --long`

- Print outdated dependencies in a specific format:

`pnpm outdated --format {{format}}`

- Print only versions that satisfy specifications in `package.json`:

`pnpm outdated --compatible`

- Check only outdated [D]ev dependencies:

`pnpm outdated --dev`
